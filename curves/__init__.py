# -*- coding: utf-8 -*-

# curves
# ------
# functional curve algebra (created by auxilium)
#
# Author:   sonntagsgesicht
# Version:  0.1.2, copyright Thursday, 10 October 2024
# Website:  https://github.com/sonntagsgesicht/curves
# License:  Apache License 2.0 (see LICENSE file)


import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())

__doc__ = 'functional curve algebra (created by auxilium)'
__license__ = 'Apache License 2.0'

__author__ = 'sonntagsgesicht'
__email__ = 'sonntagsgesicht@icloud.com'
__url__ = 'https://github.com/sonntagsgesicht/curves'

__date__ = 'Friday, 11 October 2024'
__version__ = '0.1.3'
__dev_status__ = '3 - Alpha'  # '4 - Beta'  or '5 - Production/Stable'

__dependencies__ = ()
__dependency_links__ = ()
__data__ = ()
__scripts__ = ()
__theme__ = ''

from .curves import Curve, init  # noqa F401 E402
from . import functions  # noqa F401 E402
from . import numerics  # noqa F401 E402
from .operators import Integral, Derivative  # noqa F401 E402
from .plot import plotter, plot, lin  # noqa F401 E402


γ = Curve
X = Curve('X')
