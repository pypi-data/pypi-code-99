# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cognite',
 'cognite.well_model',
 'cognite.well_model.client',
 'cognite.well_model.client.api',
 'cognite.well_model.client.api.merge_rules',
 'cognite.well_model.client.models',
 'cognite.well_model.client.utils',
 'cognite.well_model.wsfe']

package_data = \
{'': ['*']}

install_requires = \
['cognite-logger>=0.5.0,<0.6.0',
 'msal>=1.13.0,<2.0.0',
 'nulltype>=2.3.1,<3.0.0',
 'numpy>=1.18.1,<2.0.0',
 'oauthlib>=3.1.0,<4.0.0',
 'pandas>=1.0.1,<2.0.0',
 'pydantic>=1.8,<2.0',
 'pytest-mock-server>=0.2.0,<0.3.0',
 'requests-oauthlib>=1.3.0,<2.0.0',
 'requests>=2.21.0,<3.0.0']

setup_kwargs = {
    'name': 'cognite-wells-sdk',
    'version': '0.6.0b44',
    'description': '',
    'long_description': '# Installation with pip\n\n```bash\npip install cognite-wells-sdk\n```\n\n# Usage\n\n## Authenticating and creating a client\n\n### With environment variables\n\n**NOTE**: *must be valid for both cdf and geospatial API*\n\n```bash\nexport COGNITE_PROJECT=<project-tenant>\nexport COGNITE_API_KEY=<your-api-key>\n```\n\nYou can then initialize the client with\n```py\nfrom cognite.well_model import CogniteWellsClient\nwells_client = CogniteWellsClient()\n```\n\n### Without environment variables\n\nAlternatively, the client can be initialized like this:\n\n```python\nimport os\nfrom cognite.well_model import CogniteWellsClient\napi_key = os.environ["COGNITE_API_KEY"]\nwells_client = CogniteWellsClient(project="your-project", api_key=api_key)\n```\n\n## **Well queries**\n\n#### Get well by asset external id or matching id\n\n```python\n\nwell: Well = client.wells.retrieve(asset_external_id="VOLVE:15/9-F-15")\n\n# OR specify matching_id\n\nwell: Well = client.wells.retrieve(matching_id="kfe72ik")\n```\n\n#### Get multiple wells by asset external ids or matching ids\n\n```python\nwells = client.wells.retrieve_multiple(\n    asset_external_ids=["VOLVE:15/9-F-15"],\n    matching_ids=["je93kmf"]\n)\n```\n\n\n#### Delete well\n\nWarning! Note that if you delete a _well_, it will cascade to delete all _wellbores_, _measurements_, _trajectories_,\n_NPT events_, and _NDS events_ connected to that well asset.\n\n```python\nto_delete: List[AssetSource] = [AssetSource(asset_external_id="VOLVE:15/9-F-15", source_name="VOLVE")]\nclient.wells.delete(to_delete)\n```\n\n#### List wells\n\n```python\nwells = wells_client.wells.list()\n```\n\n#### Filter wells by wkt polygon\n\n```python\nfrom cognite.well_model.models import PolygonFilter\n\npolygon = \'POLYGON ((0.0 0.0, 0.0 80.0, 80.0 80.0, 80.0 0.0, 0.0 0.0))\'\nwells = wells_client.wells.filter(polygon=PolygonFilter(geometry=polygon, crs="epsg:4326"))\n```\n\n#### Filter wells by wkt polygon, name/description and specify desired outputCrs\n\n```python\npolygon = \'POLYGON ((0.0 0.0, 0.0 80.0, 80.0 80.0, 80.0 0.0, 0.0 0.0))\'\nwells = wells_client.wells.filter(\n    polygon=PolygonFilter(geometry=polygon, crs="epsg:4326", geometry_type="WKT"),\n    string_matching="16/",\n    output_crs="EPSG:23031"\n)\n```\n\n#### Get wells that have a trajectory\n\n```python\nfrom cognite.well_model.models import TrajectoryFilter\n\nwells = wells_client.wells.filter(trajectories=TrajectoryFilter(), limit=None)\n```\n\n#### Get wells that have a trajectory with data between certain depths\n\n```python\nwells = wells_client.wells.filter(trajectories=TrajectoryFilter(min_depth=1400.0, max_depth=1500.0), limit=None)\n```\n\n#### Get wells that has the right set of measurement types\n\n```python\nfrom cognite.well_model.models import MeasurementFilter, MeasurementFilters, MeasurementType\n\ngammarayFilter = MeasurementFilter(measurement_type=MeasurementType.gamma_ray)\ndensityFilter = MeasurementFilter(measurement_type=MeasurementType.density)\n\n# Get wells with all measurements\nmeasurements_filter = MeasurementFilters(contains_all=[gammarayFilter, densityFilter])\nwells = wells_client.wells.filter(measurements=measurements_filter, limit=None)\n\n# Or get wells with any of the measurements\nmeasurements_filter = MeasurementFilters(contains_any=[gammarayFilter, densityFilter])\nwells = wells_client.wells.filter(measurements=measurements_filter, limit=None)\n```\n\n#### Get wells that has right set of npt event criterias\n```python\nnpt = WellNptFilter(\n    duration=DoubleRange(min=1.0, max=30.0),\n    measuredDepth=LengthRange(min=1800.0, max=3000.0, unit=DistanceUnitEnum.meter),\n    nptCodes=ContainsAllOrAny(containsAll=["FJSB", "GSLB"]),\n    nptCodeDetails=ContainsAllOrAny(containsAll=["SLSN", "OLSF"]),\n)\n\nwell_items = client.wells.filter(npt=npt)\n```\n\n## **Wellbore queries**\n\n#### Get wellbore by asset external id or matching id\n\n```python\nwellbore: Wellbore = client.wellbores.retrieve(asset_external_id="VOLVE:15/9-F-15 A")\n\n# OR specify a matching_id\n\nwellbore: Wellbore = client.wellbores.retrieve(matching_id="32bc81ce")\n```\n\n#### Get multiple wellbores by asset external ids or matching ids\n\n```python\nwellbore_items = client.wellbores.retrieve_multiple(\n    asset_external_ids=["VOLVE:15/9-F-15 B", "VOLVE:15/9-F-15 C", "VOLVE:15/9-F-4", "VOLVE:13/10-F-11 T2"],\n    matching_ids=["2984nfe", "nfy39g", "jkey73g"]\n)\n```\n\n#### Get wellbores from a single well by asset external id or matching id\n\n```python\nwellbore_items = client.wellbores.retrieve_multiple_by_well(asset_external_id="VOLVE: WELL-202")\n\n# OR specify matching_id\n\nwellbore_items = client.wellbores.retrieve_multiple_by_well(matching_id="fok8240f")\n```\n\n## **Trajectory queries**\n\n#### Get trajectories by wellbore asset external id or matching id\n\n```python\ntrajectory_list = client.trajectories.retrieve_multiple_by_wellbore(\n    asset_external_id="VOLVE: WELLBORE-202"\n)\n\n# OR specify matching id\n\ntrajectory_list = client.trajectories.retrieve_multiple_by_wellbore(\n    matching_id="ko73kf"\n)\n```\n\n#### Get trajectories by wellbore asset external ids or matching ids\n\n```python\ntrajectory_list = client.trajectories.retrieve_multiple_by_wellbores(\n    asset_external_ids=["VOLVE: WELLBORE-201", "VOLVE: WELLBORE-202"],\n    matching_ids=["kfe7kf", "kie832"]\n)\n```\n\n#### List trajectory data\n\n```python\nrequest = TrajectoryDataRequest(\n    sequence_external_id="13/10-F-11 T2 ACTUAL",\n    measured_depth_range=DepthRange(min_depth=2, max_depth=5, unit="meter"),\n    true_vertical_depth_range=DepthRange(min_depth=0.2, max_depth=0.5, unit="meter"),\n)\ntrajectories = client.trajectories.list_data([request])\n```\n\n## **Measurement queries**\n\n#### Get multiple measurements from wellbore asset external id or matching id\n```py\nmeasurement_list = client.measurements.retrieve_multiple_by_wellbore(asset_external_id="VOLVE:WELLBORE-201")\n\n# OR specify matching_id\nmeasurement_list = client.measurements.retrieve_multiple_by_wellbore(matching_id="9u2jnf")\n```\n\n#### Get multiple measurements from wellbore asset external ids or matching ids\n```py\nvalid_wellbore_ids = ["VOLVE:WELLBORE-201", "VOLVE:WELLBORE-202"]\nmeasurement_list = client.measurements.retrieve_multiple_by_wellbores(asset_external_ids=valid_wellbore_ids)\n```\n\n#### Filter measurement data\n```py\nmeasurement_data_request = MeasurementDataRequest(\n        sequence_external_id="VOLVE:seq1",\n        measured_depth_range=DepthRange(min_depth=0.0, max_depth=10_000.0, unit="meter"),\n    )\n\nmeasurement_data_list: MeasurementDataList = client.measurements.list_data([measurement_data_request])\n```\n\n## **NPT Event queries**\n\n#### Filter NPT events\n```py\nnpt_events = client.npt.list(\n    duration=DoubleRange(min=3.0, max=10.5),\n    md=LengthRange(min=590.0, max=984.0, unit="meter"),\n    npt_codes=["O"],\n    npt_code_details=["1KFO"],\n    wellbore_asset_external_ids=["VOLVE:15/9-F-15 A", "VOLVE:15/9-F-15 D"],\n    wellbore_matching_ids=["KFOEFW"]\n)\n```\n\n#### List all NPT codes\n```py\nnpt_codes: List[str] = client.npt.codes()\n```\n\n#### List all NPT detail codes\n```py\nnpt_detail_codes: List[str] = client.npt.detail_codes()\n```\n\n## **NDS Event queries**\n\n#### Filter NDS events\n```py\nnds_events = client.nds.list(\n    hole_start=LengthRange(min=10, max=15, unit="meter"),\n    hole_end=LengthRange(min=20, max=35, unit="meter"),\n    wellbore_asset_external_ids=["VOLVE:15/9-F-15 A"],\n    wellbore_matching_ids=["KOEFKE"],\n    probabilities=[3, 5],\n    severities=[3, 5]\n)\n```\n\n#### List all NDS risk types\n```py\nrisk_types: List[str] = client.nds.risk_types()\n```\n\n## Casing queries\n\n#### Filter casings\n```py\ncasings = client.casings.list(\n    wellbore_asset_external_ids=["VOLVE:15/9-F-15 A"],\n    wellbore_matching_ids=["KOEFKE"],\n)\n```\n\n## Ingestion\n\n### Initialise tenant\n\nBefore ingesting any wells, the tenant must be initialized to add in the standard assets and labels used in the WDL.\n\n```python\nfrom cognite.well_model import CogniteWellsClient\n\nwells_client = CogniteWellsClient()\nlog_output = wells_client.ingestion.ingestion_init()\nprint(log_output)  # If something is wrong with authorization, you should see that in the logs\n```\n\n### Add source\n\nBefore ingestion from a source can take place, the source must be registered in WDL.\n\n```python\nimport os\nfrom cognite.well_model import CogniteWellsClient\n\nwells_client = CogniteWellsClient()\ncreated_sources = wells_client.sources.ingest_sources(["Source1, Source2"])\n```\n\n### Ingest wells\n```python\nimport os\nfrom datetime import date\n\nfrom cognite.well_model import CogniteWellsClient\nfrom cognite.well_model.models import DoubleWithUnit, WellDatum, Wellhead, WellIngestion\n\nwells_client = CogniteWellsClient()\nsource_asset_id = 102948135620745 # Id of the well source asset in cdf\n\nwell_to_create = WellIngestion(\n    asset_id=source_asset_id,\n    well_name="well-name",\n    description="Optional description for the well",\n    country="Norway",\n    quadrant="25",\n    block="25/5",\n    field="Example",\n    operator="Operator1",\n    spud_date=date(2021, 3, 17),\n    water_depth=0.0,\n    water_depth_unit="meters",\n    wellhead=Wellhead(\n        x = 21.0,\n        y = 42.0,\n        crs = "EPSG:4236" # Must be a EPSG code\n    ),\n    datum=WellDatum(\n        elevation = DoubleWithUnit(value=1.0, unit="meters"),\n        reference = "well-datum-reference",\n        name = "well-datum-name"\n    ),\n    source="Source System Name"\n)\n\nwells_client.ingestion.ingest_wells([well_to_create]) # Can add multiple WellIngestion objects at once\n```\n\n### Ingest wellbores with optional well and/or trajectory\n```python\nimport os\n\nfrom cognite.well_model import CogniteWellsClient\nfrom cognite.well_model.models import (\n    DoubleArrayWithUnit,\n    TrajectoryIngestion,\n    WellIngestion,\n    WellboreIngestion,\n    ParentType,\n    MeasurementIngestion,\n    MeasurementField,\n    MeasurementType\n)\n\nwells_client = CogniteWellsClient()\nsource_asset_id = 102948135620745 # Id of the wellbore source asset in cdf\nsource_trajectory_ext_id = "some sequence ext id" # Id of the source sequence in cdf\n\nwell_to_create = WellIngestion(...)\ntrajectory_to_create = TrajectoryIngestion(\n    source_sequence_ext_id=source_trajectory_ext_id,\n    measured_depths = DoubleArrayWithUnit(values=[0.0, 1.0, 2.0], unit="meters"),\n    inclinations = DoubleArrayWithUnit(values=[10.0, 1.0, 22.0], unit="degrees"),\n    azimuths = DoubleArrayWithUnit(values=[80.0, 81.0, 82.0], unit="degrees")\n)\nmeasurements_to_create = [\n    MeasurementIngestion(\n        sequence_external_id="measurement_sequence_1",\n        measurement_fields=[\n            MeasurementField(type_name=MeasurementType.gamma_ray),\n            MeasurementField(type_name=MeasurementType.density),\n        ],\n    ),\n    MeasurementIngestion(\n        sequence_external_id="measurement_sequence_2",\n        measurement_fields=[\n            MeasurementField(type_name=MeasurementType.geomechanics),\n            MeasurementField(type_name=MeasurementType.lot),\n        ],\n    )\n]\n\nwellbore_to_create = WellboreIngestion(\n    asset_id = source_asset_id,\n    wellbore_name = "wellbore name",\n    parent_name = "name of parent well or wellbore",\n    parent_type = ParentType.well, # or ParentType.wellbore\n    well_name = "name of parent well", # top level well; required in addition to the parent name (even if parent is well)\n    source = "Source System Name",\n    trajectory_ingestion = trajectory_to_create,\n    measurement_ingestions = measurements_to_create,\n    well_ingestion = well_to_create # if not ingesting a well, then one must already exist\n)\n\nwells_client.ingestion.ingest_wellbores([wellbore_to_create]) # Can add multiple WellboreIngestion objects at once\n```\n\n### Ingest casing data\n```python\nimport os\n\nfrom cognite.well_model import CogniteWellsClient\nfrom cognite.well_model.models import (\n    CasingAssembly,\n    DoubleWithUnit,\n    CasingSchematic,\n    SequenceSource,\n)\n\nclient = CogniteWellsClient()\n\ncasing_assemblies = CasingAssembly(\n    min_inside_diameter=DoubleWithUnit(value=0.1, unit="meter"),\n    min_outside_diameter=DoubleWithUnit(value=0.2, unit="meter"),\n    max_outside_diameter=DoubleWithUnit(value=0.3, unit="meter"),\n    original_measured_depth_top=DoubleWithUnit(value=100, unit="meter"),\n    original_measured_depth_base=DoubleWithUnit(value=101, unit="meter"),\n)\n\ncasing = CasingSchematic(\n    wellbore_asset_external_id="VOLVE:wb-1",\n    casing_assemblies=casing_assemblies,\n    source=SequenceSource(sequence_external_id="VOLVE:seq1", source_name="VOLVE"),\n    phase="PLANNED",\n)\nclient.casings.ingest([casing])\n```\n\n### Ingest Measurement data\n\n```python\nclient = CogniteWellsClient()\n\nseq = SequenceMeasurements(\n    wellbore_asset_external_id="VOLVE:wb-1",\n    source=SequenceSource(sequence_external_id="VOLVE:seq1", source_name="VOLVE"),\n    measured_depth=MeasuredDepthColumn(column_external_id="DEPT", unit=DistanceUnit(unit="foot")),\n    columns=[\n        SequenceMeasurementColumn(measurement_type=MeasurementType.gamma_ray, column_external_id="GR",unit="gAPI"),\n        SequenceMeasurementColumn(measurement_type=MeasurementType.resistivity_deep, column_external_id="RDEEP",unit="ohm.m")\n    ])\n\nclient.measurements.ingest([seq])\n```\n\n### Ingest NPT event data\n```python\nfrom cognite.well_model import CogniteWellsClient\n\nstart_time = 10000000000\nend_time = 20000000000\n\nnpt_events_to_ingest = [\n    NptIngestionItems(\n        wellboreName="Platform WB 12.25 in OH",\n        wellName="34/10-8",\n        npt_items=[\n            NptIngestion(\n                npt_code="EGSK",\n                npt_code_detail="FSK",\n                npt_code_level="1",\n                source_event_external_id="m2rmB",\n                source="EDM-Npt",\n                description="REAM OUT TIGHT HOLE",\n                start_time=start_time,\n                end_time=end_time,\n                location="North sea",\n                measured_depth=DoubleWithUnit(value=100.0), unit="foot"),\n                root_cause=source_event.metadata["root_cause"],\n                duration=(end_time - start_time) / (60 * 60 * 1000.0), # in hours\n                subtype="GSK"\n            )\n        ],\n    )\n]\n\nnpt_events = client.ingestion.ingest_npt_events(body)\n```\n\n### Ingest NDS event data\n```python\nfrom cognite.well_model import CogniteWellsClient\n\nstart_time = 10000000000\nend_time = 20000000000\n\nnds_events_to_ingest = [\n    NdsIngestionItems(\n        wellbore_name="Platform WB 12.25 in OH",\n        well_name="34/10-8",\n        nds_items=[\n            NdsIngestion(\n                source_event_external_id="nds-source-event",\n                source="EDM-Nds",\n                hole_start=DoubleWithUnit(value=12358.0, unit="foot"),\n                hole_end=DoubleWithUnit(value=15477.0, unit="foot"),\n                severity=1,\n                probability=1,\n                description="npt description",\n                hole_diameter=DoubleWithUnit(value=1.25, unit="inches"),\n                risk_type="Mechanical",\n                subtype="Excessive Drag",\n            )\n        ],\n    )\n]\n\nnds_events = client.ingestion.ingest_nds_events(body)\n```\n\n\n# Well structured file extractor\n\nThis SDK has a work-in-progress support for the Well Structured File Extractor\n(WSFE). The WSFE is a service with a HTTP interface that lets you extract data\nfrom LAS, LIS, ASC, and DLIS files and creates CDF squences from them.\n\n> **NB**: The API\nis subject to change, so please make sure you are using the latest version of\nthe SDK.\n\n## Usage\n\nThe arguments for creating a `WellLogExtractorClient` is the same as for\n`CogniteWellsClient` and `CogniteClient`. The example below authenticates using\na token.\n\n```py\nfrom cognite.well_model.wsfe.client import WellLogExtractorClient\nfrom cognite.well_model.wsfe.models import CdfFileLocator, CdfSource, Destination, FileType\n\nwsfe = WellLogExtractorClient(\n    client_name="test",\n    project="subsurface-test",\n    cluster="greenfield",\n    token="YOUR BEARER TOKEN\n)\n```\n\nTo use the extractor service, you must first upload some DLIS, LAS, ASC, or LIS files to CDF files.\nThen you can queue the files like this:\n\n```py\nitems = [\n    CdfFileLocator(\n        source=CdfSource(\n            file_external_id = "dlis:889",\n            file_type=FileType.dlis\n        ),\n        destination=Destination(datasetExternalId="volve"),\n        contains_trajectory = False,\n    )\n]\nstatus_map = wsfe.submit(items)\n```\n\nThe `wsfe.submit` call will return a `Dict[str, int]` response. The string is\nthe external id of the file and the int is a _process id_. To get the current status, you can run:\n\n```py\nprocess_ids = [2145596483]  # or list(status_map.values())\nresult = wsfe.status(process_ids)\nfor key, process_state in result.items():\n    log = process_state.log\n    for seq in process_state.created_sequences:\n        print("Created sequence:", seq)\n    for event in log.events:\n        print(f"{event.timestamp} [{event.severity.value}], {event.message}")\n```\nOutput might look like this:\n```\nCreated sequence: dlis:889:0:0\nCreated sequence: dlis:889:1:0\n2021-10-05 10:34:25.373653 [info], [STARTED] Downloading file from CDF\n2021-10-05 10:34:25.584203 [info], [FINISHED] Downloading file from CDF\n2021-10-05 10:34:25.584239 [info], [STARTED] Parsing file\n2021-10-05 10:34:25.791715 [info], [FINISHED] Parsing file\n2021-10-05 10:34:25.792185 [info], [STARTED] Writing 15/9-F-12 to CDF (1/2)\n...\n```\n\nCreated sequences will have metadata `creator:\n"well-structured-file-extractor"`.\n',
    'author': 'Dylan Phelps',
    'author_email': 'dylan.phelps@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
