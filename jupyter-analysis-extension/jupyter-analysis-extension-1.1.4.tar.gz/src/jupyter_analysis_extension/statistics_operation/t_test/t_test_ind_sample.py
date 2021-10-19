#!/usr/bin/env python
# coding: utf-8

import numpy.ma as ma
# Copyright (c) kyoungjun.
# Distributed under the terms of the Modified BSD License.
from scipy import stats

from jupyter_analysis_extension.statistics_operation.common_util import CommonUtil
from jupyter_analysis_extension.statistics_operation.statistic_original import StatisticOperation
from jupyter_analysis_extension.statistics_widget.common_widget import CommonWidget
from jupyter_analysis_extension.statistics_widget.t_test.t_test_ind_sample import WidgetTTestIndSample


class TTestIndSample(StatisticOperation):
    def __init__(self, df, column_type_list, refresh_tab, logger):
        self.op_name = "T-Test : Independent Sample"
        self.sub = [
            {"name": "Dependent Variable(s)", "type": ["N"], "max_count": 0, "min_count": 1},
            {"name": "Grouping Variable", "type": ["N"], "max_count": 1, "min_count": 0}
        ]
        self.option = [
            {"name": "Test Types", "type": "checkbox", "value": ['Student\'s', 'Welch\'s', 'Mann-Whitney U']},
            {"name": "Hypothesis", "type": "radio",
             "value": ["Group 1 ≠ Group 2", "Group 1 > Group 2", "Group 1 < Group 2"]}
        ]
        self.callback = {"refresh": refresh_tab}

        super(TTestIndSample, self).__init__(self.op_name, df, column_type_list, refresh_tab, logger)

    def construct_control_panel(self):
        self.control_panel, self.control_data = CommonWidget.make_control_panel(
            df=self.input_df,
            type_list=self.column_type_list,
            title=self.op_name,
            sub=self.sub,
            option=self.option,
            callback=self.callback
        )
        self.column_value = self.control_data["column"]

        self.connect_button_layout(self.control_panel.children[1], self.on_analyze_button_clicked)

    def on_analyze_button_clicked(self, widget):
        self.set_analyze_text('In progress...')

        # catch invalid data
        option = self.control_data['option']
        is_valid = self.validate_input_data(self.control_data)
        if not is_valid:
            return

        # get analysis data & option
        degree_freedom = len(self.input_df) - 2

        dependent_layout_var_list = list(self.control_data['Dependent Variable(s)'])
        dependent_var_list = []
        for layout_var in dependent_layout_var_list:
            dependent_var_list.append(self.column_value[layout_var])

        grouping_layout_var_list = list(self.control_data['Grouping Variable'])
        group_var = self.column_value[grouping_layout_var_list[0]]
        if len(self.input_df[group_var].dropna().unique()) == 1:
            self.input_df[group_var] = self.input_df[group_var].fillna('null')
        else:
            pass
        group_var_unique_list = list(self.input_df[group_var].dropna().unique())

        group_1_data_list = self.input_df[self.input_df[group_var]
                                          == group_var_unique_list[0]]
        group_2_data_list = self.input_df[self.input_df[group_var]
                                          == group_var_unique_list[1]]

        tests_students = option['Test Types']['Student\'s']
        tests_welchs = option['Test Types']['Welch\'s']
        tests_mannwhitneyu = option['Test Types']['Mann-Whitney U']

        hypothesis_alternative = option['Hypothesis']['radio']
        if hypothesis_alternative == 'Group 1 ≠ Group 2':
            hypothesis_alternative = 'two-sided'
        elif hypothesis_alternative == 'Group 1 > Group 2':
            hypothesis_alternative = 'greater'
        elif hypothesis_alternative == 'Group 1 < Group 2':
            hypothesis_alternative = 'less'

        result_widgets = self.get_result_widgets(
            degree_freedom, dependent_var_list, [group_1_data_list, group_2_data_list], group_var_unique_list,
            [tests_students, tests_welchs, tests_mannwhitneyu], [hypothesis_alternative])

        CommonUtil.update_result_layout(self.control_panel, result_widgets)

        self.set_analyze_text('Done.')

    def validate_input_data(self, control_data):
        error_msg = CommonUtil.check_variables_shapes(control_data, 'Dependent Variable(s)', 'Number',
                                                      self.column_type_list, self.column_value, self.sub)
        if error_msg is not None:
            self.set_analyze_text(error_msg, 'warning')
            return False

        error_msg = CommonUtil.check_option_checkbox(control_data, 'Test Types', 1)
        if error_msg is not None:
            self.set_analyze_text(error_msg, 'warning')
            return False

        error_msg = CommonUtil.check_variables_shapes(control_data, 'Grouping Variable',
                                                      ['2-Category'],
                                                      self.column_type_list, self.column_value, self.sub)
        if error_msg is not None:
            self.set_analyze_text(error_msg, 'warning')
            return False

        return True

    def get_result_widgets(self, degree_freedom, dependent_var_list, grouped_df, group_var_unique_list, tests_options,
                           hypothesis_options):
        target_column_names = []
        statistic_tests_options = []
        statistic_chart = []
        statistic_result = []

        for item in dependent_var_list:
            chart_data = []
            target_column_names.append(item)
            chart_data.append(grouped_df[0][item])
            chart_data.append(grouped_df[1][item])
            if tests_options[0]:
                test_result = stats.ttest_ind(
                    grouped_df[0][item], grouped_df[1][item], equal_var=True, nan_policy='omit',
                    alternative=hypothesis_options[0])
                if ma.is_masked(test_result.statistic):
                    self.set_analyze_text('Invalid input fot t-test (Complete Bias)', 'warning')
                else:
                    target_column_names.append('')
                    statistic_result.append(test_result)
                    statistic_tests_options.append('Student\'s')

            if tests_options[1]:
                test_result = stats.ttest_ind(
                    grouped_df[0][item], grouped_df[1][item], equal_var=False, nan_policy='omit',
                    alternative=hypothesis_options[0])
                if ma.is_masked(test_result.statistic):
                    self.set_analyze_text('Invalid input fot t-test (Complete Bias)', 'warning')
                else:
                    target_column_names.append('')
                    statistic_result.append(test_result)
                    statistic_tests_options.append('Welch\'s')

            if tests_options[2]:
                if len(grouped_df[0][item].dropna()) < 1 or len(grouped_df[1][item].dropna()) < 1:
                    self.set_analyze_text('Invalid input fot t-test (Complete Bias)', 'warning')
                else:
                    test_result = stats.mannwhitneyu(
                        grouped_df[0][item].dropna(), grouped_df[1][item].dropna(),
                        alternative=hypothesis_options[0])
                    target_column_names.append('')
                    statistic_result.append(test_result)
                    statistic_tests_options.append('Mann-Whitney U')

            statistic_chart.append(chart_data)
            target_column_names.pop()

        statistic_result_table = WidgetTTestIndSample.get_statistic_result_table(
            target_column_names, degree_freedom, statistic_result, statistic_tests_options)

        plot_names = ['Box Plot (' + name + ')' for name in dependent_var_list]
        if len(self.input_df) > 10000:
            # Sampling only 10000 rows
            for index, name in enumerate(plot_names):
                plot_names[index] += name + " (Sampling 10000 rows)"
            for index, df in enumerate(statistic_chart):
                statistic_chart[index] = df.copy().sample(n=10000, random_state=1, replace=False)

        box_plot_plotly = WidgetTTestIndSample.get_box_plot_plotly(
            statistic_chart, dependent_var_list, group_var_unique_list)
        plot_names = ['Box Plot (' + name + ')' for name in dependent_var_list]
        return CommonWidget.get_accordion_widget([statistic_result_table] + box_plot_plotly,
                                                 ['Test Result(s)'] + plot_names)
