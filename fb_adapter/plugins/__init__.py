# -*- coding: UTF-8 -*-
from __future__ import absolute_import, with_statement
from . import *

_plugins = []

def register(module):
	if module not in _plugins:
		_plugins.append(module)
	