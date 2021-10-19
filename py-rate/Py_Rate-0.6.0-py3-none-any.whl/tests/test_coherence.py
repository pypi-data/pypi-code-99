#   This Python module is part of the PyRate software package.
#
#   Copyright 2020 Geoscience Australia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
This Python module contains tests for the coherence.py PyRate module.
"""
import shutil
import os
import stat
import tempfile
import numpy as np
from osgeo import osr
from osgeo import gdal
from pathlib import Path
from copy import copy

import pyrate.constants as c
import pyrate.core.prepifg_helper
import pyrate.core.shared
from pyrate.core.shared import Ifg
from pyrate.core import gdal_python
from pyrate.core import ifgconstants as ifc
from pyrate.configuration import MultiplePaths, Configuration
from pyrate import conv2tif

from tests import common


def test_small_data_coherence(gamma_or_mexicoa_conf):
    temp_obs_dir = Path(tempfile.mkdtemp())
    params = common.manipulate_test_conf(conf_file=gamma_or_mexicoa_conf, temp_obs_dir=temp_obs_dir)

    params[c.COH_MASK] = 1

    ifg_multilist = copy(params[c.INTERFEROGRAM_FILES])
    conv2tif.main(params)

    for i in ifg_multilist:
        p = Path(i.converted_path)
        p.chmod(0o664)  # assign write permission as conv2tif output is readonly
        ifg = pyrate.core.shared.dem_or_ifg(data_path=p.as_posix())
        if not isinstance(ifg, Ifg):
            continue
        ifg.open()
        # now do coherence masking and compare
        ifg = pyrate.core.shared.dem_or_ifg(data_path=p.as_posix())
        ifg.open()
        converted_coh_file_path = pyrate.core.prepifg_helper.coherence_paths_for(p, params, tif=True)
        gdal_python.coherence_masking(ifg.dataset,
                                      coh_file_path=converted_coh_file_path,
                                      coh_thr=params[c.COH_THRESH]
                                      )
        nans = np.isnan(ifg.phase_data)
        coherence_path = pyrate.core.prepifg_helper.coherence_paths_for(p, params, tif=True)
        cifg = Ifg(coherence_path)
        cifg.open()
        cifg_below_thrhold = cifg.phase_data < params[c.COH_THRESH]
        np.testing.assert_array_equal(nans, cifg_below_thrhold)
    shutil.rmtree(temp_obs_dir)


def test_coherence_files_not_converted():
    # define constants
    NO_DATA_VALUE = 0
    driver = gdal.GetDriverByName('GTiff')

    # create a sample gdal dataset

    # sample gdal dataset
    sample_gdal_filename = "dataset_01122000.tif"
    options = ['PROFILE=GeoTIFF']
    sample_gdal_dataset = driver.Create(sample_gdal_filename, 5, 5, 1, gdal.GDT_Float32, options=options)
    srs = osr.SpatialReference()
    wkt_projection = srs.ExportToWkt()
    sample_gdal_dataset.SetProjection(wkt_projection)

    sample_gdal_band = sample_gdal_dataset.GetRasterBand(1)
    sample_gdal_band.SetNoDataValue(NO_DATA_VALUE)
    sample_gdal_band.WriteArray(np.arange(25).reshape(5, 5))
    sample_gdal_dataset.SetMetadataItem(ifc.FIRST_DATE, '2019-10-20')
    sample_gdal_dataset.SetMetadataItem(ifc.SECOND_DATE, '2019-11-01')
    sample_gdal_dataset.SetMetadataItem(ifc.PYRATE_WAVELENGTH_METRES, '10.05656')
    sample_gdal_dataset.FlushCache()
    sample_gdal_dataset = None
    ifg = Ifg(sample_gdal_filename)
    ifg.open()

    # create a coherence mask dataset
    tmpdir = tempfile.mkdtemp()
    out_dir = Path(tmpdir)  # we won't be creating any output coherence mask files as there are already GeoTIFFs
    params = common.min_params(out_dir)
    coherence_mask_filename = MultiplePaths(Path("mask_dataset_01122000-02122000.tif").as_posix(), params)
    coherence_mask_dataset = driver.Create(coherence_mask_filename.converted_path, 5, 5, 1, gdal.GDT_Float32)
    srs = osr.SpatialReference()
    wkt_projection = srs.ExportToWkt()
    coherence_mask_dataset.SetProjection(wkt_projection)
    coherence_mask_band = coherence_mask_dataset.GetRasterBand(1)
    coherence_mask_band.SetNoDataValue(NO_DATA_VALUE)
    arr = np.arange(0, 75, 3).reshape(5, 5) / 100.0
    arr[3, 4] = 0.25  # insert some random lower than threshold number
    arr[4, 2] = 0.20  # insert some random lower than threshold number

    coherence_mask_band.WriteArray(arr)
    # del the tmp handler datasets created
    del coherence_mask_dataset
    # create an artificial masked dataset
    expected_result_array = np.nan_to_num(
        np.array(
            [
                [np.nan, np.nan, np.nan, np.nan, np.nan],
                [np.nan, np.nan, np.nan, np.nan, np.nan],
                [10.0, 11.0, 12.0, 13.0, 14.0],
                [15.0, 16.0, 17.0, 18.0, np.nan],
                [20.0, 21.0, np.nan, 23.0, 24.0],
            ]
        )
    )

    # use the gdal_python.coherence_masking to find the actual mask dataset
    coherence_thresh = 0.3

    gdal_python.coherence_masking(ifg.dataset, coherence_mask_filename.converted_path, coherence_thresh)

    sample_gdal_array = np.nan_to_num(ifg.phase_data)

    # compare the artificial masked and actual masked datasets
    np.testing.assert_array_equal(sample_gdal_array, expected_result_array)

    # del the tmp datasets created
    os.remove(coherence_mask_filename.converted_path)

    ifg.close()
    os.remove(sample_gdal_filename)
