import numpy as np
import straxen
import tempfile
import os
import unittest
import shutil
import uuid


test_run_id_1T = '180423_1021'


class TestBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        temp_folder = uuid.uuid4().hex
        # Keep one temp dir because we don't want to download the data every time.
        cls.tempdir = os.path.join(tempfile.gettempdir(), temp_folder)
        assert not os.path.exists(cls.tempdir)

        print("Downloading test data (if needed)")
        st = straxen.contexts.demo()
        cls.run_id = test_run_id_1T
        cls.st = st

    @classmethod
    def tearDownClass(cls):
        # Make sure to only cleanup this dir after we have done all the tests
        if os.path.exists(cls.tempdir):
            shutil.rmtree(cls.tempdir)

    def test_run_selection(self):
        st = self.st
        # Ignore strax-internal warnings
        st.set_context_config({'free_options': tuple(st.config.keys())})

        run_df = st.select_runs(available='raw_records')
        print(run_df)
        run_id = run_df.iloc[0]['name']
        assert run_id == test_run_id_1T

    def test_processing(self):
        st = self.st
        df = st.get_df(self.run_id, 'event_info')

        assert len(df) > 0
        assert 'cs1' in df.columns
        assert df['cs1'].sum() > 0
        assert not np.all(np.isnan(df['x'].values))

    def test_get_livetime_sec(self):
        st = self.st
        events = st.get_array(self.run_id, 'peaks')
        straxen.get_livetime_sec(st, test_run_id_1T, things=events)

    def test_mini_analysis(self):
        @straxen.mini_analysis(requires=('raw_records',))
        def count_rr(raw_records):
            return len(raw_records)

        n = self.st.count_rr(self.run_id)
        assert n > 100

    def test_extract_latest_comment(self,
                                    context='xenonnt_online',
                                    test_for_target='raw_records',
                                    ):
        if context == 'xenonnt_online' and not straxen.utilix_is_configured():
            return
        st = getattr(straxen.contexts, context)()
        assert hasattr(st, 'extract_latest_comment'), "extract_latest_comment not added to context?"
        st.extract_latest_comment()
        assert st.runs is not None, "No registry build?"
        assert 'comments' in st.runs.keys()
        st.select_runs(available=test_for_target)
        if context == 'demo':
            assert len(st.runs)
        assert f'{test_for_target}_available' in st.runs.keys()

    def test_extract_latest_comment_lone_hits(self):
        """Run the test for some target that is not in the default availability check"""
        self.test_extract_latest_comment(test_for_target='lone_hits')

    def test_extract_latest_comment_demo(self):
        self.test_extract_latest_comment(context='demo')
