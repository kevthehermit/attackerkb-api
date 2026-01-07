#!/usr/bin/env python

__title__ = "attackerkb-api"
__version__ = "0.0.1"
__author__ = "Kevin Breen"
__license__ = "MIT"
__copyright__ = 'Copyright (C) 2020 Kev "thehermit" Breen'

from .api import ApiError as ApiError
from .api import AttackerKB as AttackerKB

__all__ = ["ApiError", "AttackerKB"]
