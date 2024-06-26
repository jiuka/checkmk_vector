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

from pathlib import Path
from typing import Any

from .bakery_api.v1 import FileGenerator, OS, Plugin, register


def get_vector_plugin_files(conf: Any) -> FileGenerator:
    yield Plugin(
        base_os=OS.LINUX,
        source=Path('vector.py'),
        target=Path('vector.py')
    )


register.bakery_plugin(
    name='vector',
    files_function=get_vector_plugin_files,
)
