"""chartjs module"""

from dataclasses import dataclass
import json
from typing import Generator
from uuid import uuid4
from matatika.metadata import ChartJSMetadata
from matatika.dataset import Dataset


def to_chart(dataset: Dataset, data: list=None):
    """Converts dataset data and metadata to the Chart.js specification"""

    if not data:
        data = json.loads(dataset.raw_data)

    if not dataset.metadata or not data:
        return None

    visualisation = json.loads(dataset.visualisation)
    chartjs_chart = visualisation['chartjs-chart']
    chart_type = chartjs_chart['chartType']
    metadata = ChartJSMetadata.from_str(dataset.metadata)

    # collect data with common column names
    formatted_data = {k: [] for k in data[0].keys()}
    row: dict
    for row in data:
        for column_name, column_data in row.items():
            formatted_data[column_name].append(column_data)

    chart_datasets = []
    chart_labels = []
    chart_options = chartjs_chart.get('options')

    if chart_type in ('pie', 'doughnut'):

        chart_datasets, chart_labels, chart_options_default = _to_circle_chart(
            formatted_data, metadata)

    # any other chart type
    else:

        # process area and scatter charts as a line chart
        if chart_type in ('area', 'scatter'):
            chart_type = 'line'

        chart_datasets, chart_labels, chart_options_default = _to_line_chart(
            formatted_data, metadata)

    return {
        'data': {
            'datasets': chart_datasets,
            'labels': chart_labels
        },
        'chart_type': chart_type,
        'options': chart_options or chart_options_default
    }


def _to_line_chart(data: dict, metadata: ChartJSMetadata):

    datasets = []
    labels = []

    tick_config = {
        'ticks': {
            'beginAtZero': True
        }
    }
    options = {
        'xAxes': [tick_config],
        'yAxes': [tick_config]
    }

    metadata_column_names = [c['name'] for c in metadata.columns]
    metadata_aggregate_names = [a['name'] for a in metadata.aggregates]

    colours = ColourPalette.get_colours()

    for column_full_name, column_data in data.items():

        column_name = metadata.remove_basename(column_full_name)
        # aggregate data
        if column_name in metadata_aggregate_names:
            label = metadata.get_label(column_full_name)

            if not label:
                label = column_full_name

            chartjs_dataset = ChartJSDataset(
                column_data,
                label,
                colours=next(colours)
            )

            datasets.append(chartjs_dataset.to_dict())

        # column data
        elif column_name in metadata_column_names:
            if labels:
                labels = [
                    "-".join((label, str(data)))[:50] for label, data in zip(labels, column_data)]
            else:
                labels = [str(label)[:50] for label in column_data]

    return datasets, labels, options


def _to_circle_chart(data: dict, metadata: ChartJSMetadata) -> Generator:

    datasets = []
    labels = []
    options = None

    dataset_data = []
    for column_name, column_data in data.items():
        label = metadata.get_label(column_name)

        if not label:
            label = column_name

        dataset_data.append(column_data)
        labels.append(label)

    chartjs_dataset = ChartJSDataset(dataset_data, circle_chart=True)

    datasets = [chartjs_dataset.to_dict()]

    return datasets, labels, options


@dataclass
class RGBColour():
    """Class for a single RGB colour"""

    red: int = 255
    green: int = 171
    blue: int = 43
    name: str = None

    def to_rgba_string(self, alpha: float = 1) -> str:
        """Converts the colour into an RGBA string notation"""

        values = ', '.join(map(str, (self.red, self.green, self.blue, alpha)))
        return f'rgba({values})'


@dataclass
class ColourPalette:
    """Colour palette for chart datasets"""

    # https://coolors.co/ff6384-36a2eb-ffce56-4bc0c0-9966ff-ff9f40-3869c9-e6254e-352cab-fa6b0c
    colours: tuple = (
        RGBColour(255, 99, 132, 'brink pink'),
        RGBColour(54, 162, 235, 'carolina blue'),
        RGBColour(255, 206, 86, 'maize crayola'),
        RGBColour(75, 192, 192, 'maximum blue green'),
        RGBColour(153, 102, 255, 'medium purple'),
        RGBColour(255, 159, 64, 'deep saffron'),
        RGBColour(56, 105, 201, 'true blue'),
        RGBColour(230, 37, 79, 'amaranth'),
        RGBColour(172, 237, 43, 'green lizard'),
        RGBColour(250, 107, 12, 'safety orange blaze orange'),
        RGBColour(70, 189, 84, 'dark pastel green'),
        RGBColour(53, 44, 171, 'blue pigment')
    )

    @classmethod
    def get_colours(cls) -> tuple:
        """Returns a background and border colour set"""

        colour_index = 0

        while True:
            colour: RGBColour = cls.colours[colour_index % len(cls.colours)]
            bg_colour = colour.to_rgba_string(0.2)
            border_colour = colour.to_rgba_string()

            yield (bg_colour, border_colour)

            colour_index += 1

# pylint: disable=too-many-instance-attributes,too-few-public-methods


class ChartJSDataset:
    """Class to handle datasets within a Chart.js chart"""

    def __init__(self,
                 data: list,
                 label: str = None,
                 colours: Generator = ColourPalette.get_colours(),
                 circle_chart: bool = False):

        self.data = data
        self.label = label

        self.id_ = str(uuid4())
        self.extra_properties = {}

        border_width = 1

        if circle_chart:
            self.bg_colour = []
            self.border_colour = []
            self.border_width = []

            for _ in range(len(self.data)):
                bg_colour, border_colour = next(colours)
                self.bg_colour.append(bg_colour)
                self.border_colour.append(border_colour)
                self.border_width.append(border_width)

        else:
            self.bg_colour, self.border_colour = colours
            self.border_width = border_width

    def to_dict(self):
        """Converts the object into a dictionary conforming to the Chart.js specification"""

        dict_ = {
            'data': self.data,
            'label': self.label,
            'backgroundColor': self.bg_colour,
            'fill': False,
            'borderColor': self.border_colour,
            'borderWidth': self.border_width
        }

        dict_ = {k: v for k, v in dict_.items() if v is not None}

        return {**dict_, **self.extra_properties}
