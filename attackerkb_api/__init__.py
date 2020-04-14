 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'attackerkb-api'
__version__ = '0.0.1'
__author__ = 'Kevin Breen'
__license__ = 'MIT'
__copyright__ = 'Copyright (C) 2020 Kev "thehermit" Breen'

try:
    import requests
except ImportError:
    pass

from .api import ApiError, AttackerKB
