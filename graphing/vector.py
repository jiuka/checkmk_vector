#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#
# Copyright (C) 2024  Marius Rieder <marius.rieder@durchmesser.ch>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from cmk.graphing.v1.metrics import (
    Metric,
    Unit,
    DecimalNotation,
    Color,
    Title,
    StrictPrecision,
)
from cmk.graphing.v1.graphs import (
    Graph
)
from cmk.graphing.v1.perfometers import (
    Perfometer,
    FocusRange,
    Closed,
    Open,
)

metric_vector_source = Metric(
    name='vector_source',
    title=Title('Sources'),
    unit=Unit(DecimalNotation(""), StrictPrecision(0)),
    color=Color.BLUE,
)

metric_vector_transform = Metric(
    name='vector_transform',
    title=Title('Transforms'),
    unit=Unit(DecimalNotation(""), StrictPrecision(0)),
    color=Color.ORANGE,
)

metric_vector_sink = Metric(
    name='vector_sink',
    title=Title('Sinks'),
    unit=Unit(DecimalNotation(""), StrictPrecision(0)),
    color=Color.GREEN,
)

graph_vector = Graph(
    name='vector',
    title=Title('Vector'),
    compound_lines=[
        'vector_source',
        'vector_transform',
        'vector_sink',
    ],
)

perfometer_vector = Perfometer(
    name='vector',
    focus_range=FocusRange(Closed(0), Open(1)),
    segments=[
        'vector_source',
        'vector_transform',
        'vector_sink',
    ],
)
