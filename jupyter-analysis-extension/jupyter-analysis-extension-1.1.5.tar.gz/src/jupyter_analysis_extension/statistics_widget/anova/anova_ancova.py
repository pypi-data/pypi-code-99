#!/usr/bin/env python
# coding: utf-8

# Copyright (c) TmaxBI.
# Distributed under the terms of the Modified BSD License.
import ipywidgets as widgets

# Graph
import plotly.graph_objs as go


class WidgetANOVAANCOVA:
    @ staticmethod
    def get_statistic_result_table(table, degree_freedom, test_type):
        res_table_info = ''
        target_degree_freedom = degree_freedom


        '''
        statistic_value = round(item.statistic, 3)
        if statistic_tests_options[pairindex] == 'Welch\'s' or statistic_tests_options[pairindex] == 'Fisher\'s':
            target_degree_freedom = '-'

        if statistic_tests_options[pairindex] == 'Fisher\'s':
            statistic_value = '{0:e}'.format(item.statistic)

        res_table_info += """
                    <tr>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td>{2}</td>
                        <td>{3}</td>
                        <td>{4}</td>
                    </tr>
                    """.format(name[pairindex], statistic_tests_options[pairindex], statistic_value,
                               target_degree_freedom, round(item.pvalue, 3))

        res_table = widgets.HTML(
            value="""
                <table style="width:100%">
                <tr style="border-bottom: 1px solid black;">
                    <th></th>
                    <th></th>
                    <th>Statistic</th>
                    <th>df</th>
                    <th>p-value</th>
                </tr>
               {0}
                </table>""".format(res_table_info),
            disabled=True
        )
        '''
        res_table = widgets.HTML(table.to_html())
        statistic_result_table = widgets.VBox([res_table])
        statistic_result_table.add_class('styledTable')

        return statistic_result_table

    @staticmethod
    def get_boxplot_sns(grouped_data, group_val_distinct):
        fig = go.FigureWidget()
        for data, index in zip(grouped_data, group_val_distinct):
            fig.add_trace(go.Box(y=data, name=index))

        fig.update_layout(
            width=500,
            height=500,
        )
        return fig