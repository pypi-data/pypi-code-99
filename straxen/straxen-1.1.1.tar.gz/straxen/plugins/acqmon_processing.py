import strax
import straxen
import numba
import numpy as np

export, __all__ = strax.exporter()

__all__ += ['T_NO_VETO_FOUND']
# Runs are usually 1 hour long, if veto is that far we don't really care
T_NO_VETO_FOUND = int(3.6e+12)


# More info about the acquisition monitor can be found here:
# https://xe1t-wiki.lngs.infn.it/doku.php?id=xenon:xenon1t:alexelykov:acquisition_monitor


@export
@strax.takes_config(strax.Option('hit_min_amplitude_aqmon', default=50, track=True,
                                 help='Minimum hit threshold in ADC*counts above baseline'),
                    strax.Option('baseline_samples_aqmon', default=10, track=True,
                                 help='Number of samples to use at the start of the pulse to determine the baseline'))
class AqmonHits(strax.Plugin):
    """ Find hits in acquisition monitor data. These hits could be 
        then used by other plugins for deadtime calculations, 
        GPS SYNC analysis, etc.
    """
    __version__ = '0.0.6'

    depends_on = ('raw_records_aqmon')
    provides = ('aqmon_hits')
    data_kind = ('aqmon_hits')

    dtype = strax.hit_dtype

    save_when = strax.SaveWhen.TARGET

    def compute(self, raw_records_aqmon):
        rec = strax.raw_to_records(raw_records_aqmon)
        strax.sort_by_time(rec)
        strax.zero_out_of_bounds(rec)
        strax.baseline(rec, baseline_samples=self.config['baseline_samples_aqmon'], flip=True)
        aqmon_hits = strax.find_hits(rec, min_amplitude=self.config['hit_min_amplitude_aqmon'])
        return aqmon_hits


# ### Veto hardware ###:
# V1495 busy veto module:
# Generates a 25 ns NIM pulse whenever a veto begins and a 25 ns NIM signal when it ends.
# A new start signal can occur only after the previous busy instance ended.
# 1ms (1e6 ns) - minimum busy veto length, or until the board clears its memory

# DDC10 High Energy Veto:
# 10ms (1e7 ns) - fixed HE veto length in XENON1T DDC10,
# in XENONnT it will be calibrated based on the length of large S2 SE tails
# The start/stop signals for the HEV are generated by the V1495 board


@export
@strax.takes_config(
    strax.Option('max_veto_window', default=int(5e8), track=True, type=int,
                 help='Maximum separation between veto stop and start pulses [ns]'),
)
class VetoIntervals(strax.OverlapWindowPlugin):
    """ Find pairs of veto start and veto stop signals and the veto duration between them
    busy_*  <= V1495 busy veto for tpc channels
    he_*    <= V1495 busy veto for high energy tpc channels
    hev_*   <= DDC10 hardware high energy veto
    """

    __version__ = '0.1.6'
    depends_on = ('aqmon_hits')
    provides = ('veto_intervals')
    data_kind = ('veto_intervals')

    def infer_dtype(self):
        dtype = [(('veto interval [ns]', 'veto_interval'), np.int64),
                 (('veto signal type', 'veto_type'), np.str_('U9'))]
        dtype += strax.time_fields
        return dtype

    def setup(self):
        self.veto_names = ['busy_', 'he_', 'hev_']
        self.channel_map = {name: ch + straxen.n_hard_aqmon_start for ch, name in
                            enumerate(['sum_wf', 'm_veto_sync',
                                       'hev_stop', 'hev_start',
                                       'he_stop', 'he_start',
                                       'busy_stop', 'busy_start'])}

    def get_window_size(self):
        # Give a very wide window
        return int(self.config['max_veto_window'] * 100)

    def compute(self, aqmon_hits, start, end):
        hits = aqmon_hits
        result = np.zeros(len(aqmon_hits) * len(self.veto_names), self.dtype)
        vetos_seen = 0

        for name in self.veto_names:
            veto_hits_start = channel_select_(hits, self.channel_map[name + 'start'])
            veto_hits_stop = channel_select_(hits, self.channel_map[name + 'stop'])

            # Here we rely on the fact that for each start, there is a single stop that
            # follows it in time. If this is not true, our hardware does not work.
            if len(veto_hits_start):
                for t, time in enumerate(veto_hits_start['time']):
                    # Find the time of stop_j that is closest to time of start_i
                    inx = np.searchsorted(veto_hits_stop['time'], time, side='right')

                    if inx == len(veto_hits_stop['time']):
                        continue
                    else:
                        result['veto_interval'][vetos_seen] = veto_hits_stop['time'][inx] - time
                        result["time"][vetos_seen] = time
                        assert time < veto_hits_stop['time'][inx]
                        result["endtime"][vetos_seen] = veto_hits_stop['time'][inx]
                        result["veto_type"][vetos_seen] = name + 'veto'
                        vetos_seen += 1
        result = result[:vetos_seen]
        result['time'] = np.clip(result['time'], start, end)
        result['endtime'] = np.clip(strax.endtime(result), 0, end)
        sort = np.argsort(result['time'])
        result = result[sort]
        return result


@numba.njit
def channel_select_(rr, ch):
    """Return data from start/stop veto channel in the acquisition monitor (AM)"""
    return rr[rr['channel'] == ch]


@export
@strax.takes_config(
    strax.Option('veto_proximity_window', default=int(5e8), type=int, track=True,
                 help='Maximum separation between veto stop and start pulses [ns]'))
class VetoProximity(strax.OverlapWindowPlugin):
    """
    Find the closest next/previous veto start and end to each event center.

    previous_x: Time in ns between the time center of an event and the previous x
    next_x: Time in ns between the time center of an event and the next x
    This also considers any x inside the event. x could be either:
        - busy_x: busy on/off signal
        - he_x:   high energy channels busy on/off signal
        - hev_x:  high energy veto on/off signal
    """

    __version__ = '0.1.2'
    depends_on = ('event_basics', 'aqmon_hits')
    provides = ('veto_proximity')
    data_kind = ('events')
    save_when = strax.SaveWhen.TARGET
    veto_names = ['busy', 'he', 'hev']

    def infer_dtype(self):
        dtype = []
        for n in self.veto_names:
            dtype += [
                ((f'Time to previous {n} veto start [ns]', f'previous_{n}_on'), np.int64),
                ((f'Time to previous {n} veto end [ns]', f'previous_{n}_off'), np.int64),
                ((f'Time to next {n} veto start [ns]', f'next_{n}_on'), np.int64),
                ((f'Time to next {n} veto end [ns]', f'next_{n}_off'), np.int64),
                ]
        dtype += strax.time_fields
        return dtype

    def setup(self):
        self.channel_map = {name: ch + straxen.n_hard_aqmon_start for ch, name in
                            enumerate(['sum_wf', 'm_veto_sync',
                                       'hev_stop', 'hev_start',
                                       'he_stop', 'he_start',
                                       'busy_stop', 'busy_start'])}
        self.states = ['on', 'off']

    def get_window_size(self):
        return int(self.config['veto_proximity_window'] * 100)

    def compute(self, events, aqmon_hits):
        result = np.zeros(len(events), self.dtype)
        t_event_centers = (events['time'] + events['endtime']) // 2

        for name in self.veto_names:
            # For each state find the next and previous veto
            for state in self.states:
                prev = f'previous_{name}_{state}'
                nxt = f'next_{name}_{state}'

                if state == 'on':
                    aqmon_chan = self.channel_map[f'{name}_start']
                else:
                    aqmon_chan = self.channel_map[f'{name}_stop']
                veto_start_time_selection = aqmon_hits[aqmon_hits['channel'] == aqmon_chan]['time']

                inx = 0
                for event_i, event_center in enumerate(t_event_centers):
                    if len(veto_start_time_selection):
                        inx = np.searchsorted(veto_start_time_selection, event_center, side='right')

                    # Time to previous veto on/off
                    # Just using a huge value that will not fit in any potential
                    # DAQVetoCut range
                    if inx == 0:
                        previous_veto = T_NO_VETO_FOUND
                    else:
                        previous_veto = event_center - veto_start_time_selection[inx - 1]
                    # Time to next veto on/off
                    if inx == len(veto_start_time_selection):
                        next_veto = T_NO_VETO_FOUND
                    else:
                        next_veto = veto_start_time_selection[inx] - event_center

                    result[event_i][prev] = previous_veto
                    result[event_i][nxt] = next_veto

        # Add the events time and endtime to the final result
        result['time'] = events['time']
        result['endtime'] = events['endtime']
        return result
