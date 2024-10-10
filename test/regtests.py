# -*- coding: utf-8 -*-

# auxilium
# --------
# A Python project for an automated test and deploy toolkit - 100%
# reusable.
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Sunday, 11 October 2020
# Website:  https://github.com/sonntagsgesicht/auxilium
# License:  Apache License 2.0 (see LICENSE file)


from regtest import RegressionTestCase

# first run will build reference values (stored in files)
# second run will test against those reference values
# to update reference values simply remove the according files

from curves import X
from curves.plot import lin


class CurveRegTests(RegressionTestCase):

    def setUp(self):
        self.x = lin(-10, 10)

    def test_X(self):

        def f(x):
            return 1 + 2 * x + 3 * x ** 2 + -(x / 2 - 1)

        p = 1 + 2 * X + 3 * X ** 2 + -(X / 2 - 1)

        for x in self.x:
            self.assertAlmostRegressiveEqual(f(x))
            self.assertAlmostRegressiveEqual(p(x))
