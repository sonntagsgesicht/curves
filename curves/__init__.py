# -*- coding: utf-8 -*-

# curves
# ------
# functional curve algebra (created by auxilium)
#
# Author:
# Version:  0.1, copyright Thursday, 10 October 2024
# Website:  https://github.com//curves
# License:  Apache License 2.0 (see LICENSE file)


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__doc__ = 'functional curve algebra (created by auxilium)'
__license__ = 'Apache License 2.0'

__author__ = ''
__email__ = ''
__url__ = 'https://github.com//curves'

__date__ = 'Thursday, 10 October 2024'
__version__ = '0.1'
__dev_status__ = '3 - Alpha'  # '4 - Beta'  or '5 - Production/Stable'

__dependencies__ = ()
__dependency_links__ = ()
__data__ = ()
__scripts__ = ()
__theme__ = ''

from .curves import γ, Curve  # noqa F401 E402
from . import math  # noqa F401 E402
from . import operators  # noqa F401 E402
from .plot import plotter  # noqa F401 E402

X = Curve('X')
