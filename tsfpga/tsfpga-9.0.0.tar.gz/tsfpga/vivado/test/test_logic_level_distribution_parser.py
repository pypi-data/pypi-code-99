# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the tsfpga project.
# https://tsfpga.com
# https://gitlab.com/tsfpga/tsfpga
# --------------------------------------------------------------------------------------------------

from tsfpga.vivado.logic_level_distribution_parser import LogicLevelDistributionParser


def test_get_table():
    report = """

1. Logic Level Distribution
---------------------------

+-----------------+-------------+-----+----+---+----+
| End Point Clock | Requirement |  0  |  1 | 2 |  3 |
+-----------------+-------------+-----+----+---+----+
| clk_fpga_0      | 2.000ns     | 491 | 12 | 1 | 11 |
+-----------------+-------------+-----+----+---+----+
* Columns represent the logic levels per end point clock
** Distribution is for top worst 1000 paths
"""
    expected = """\
+-----------------+-------------+-----+----+---+----+
| End Point Clock | Requirement |  0  |  1 | 2 |  3 |
+-----------------+-------------+-----+----+---+----+
| clk_fpga_0      | 2.000ns     | 491 | 12 | 1 | 11 |
+-----------------+-------------+-----+----+---+----+\
"""
    assert LogicLevelDistributionParser.get_table(report) == expected


def test_get_maximum_logic_level():
    table = """\
+-----------------+-------------+-----+----+---+----+
| End Point Clock | Requirement |  0  |  1 | 2 |  3 |
+-----------------+-------------+-----+----+---+----+
| clk_fpga_0      | 2.000ns     | 491 | 12 | 1 | 11 |
+-----------------+-------------+-----+----+---+----+\
"""
    assert LogicLevelDistributionParser.get_maximum_logic_level(table) == 3

    table = """\
+-----------------+-------------+-----+----+---+----+
| End Point Clock | Requirement |  0  |  1 | 2 |  7 |
+-----------------+-------------+-----+----+---+----+
| clk_fpga_0      | 2.000ns     | 491 | 12 | 1 | 11 |
+-----------------+-------------+-----+----+---+----+\
"""
    assert LogicLevelDistributionParser.get_maximum_logic_level(table) == 7
