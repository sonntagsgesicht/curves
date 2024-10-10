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

from copy import copy
from unittest import TestCase

from curves import X, Curve
from curves.plot import lin


class CurveTestCase(TestCase):
    def setUp(self):
        self.x = lin(-10, 10)

    def test_X(self):

        def f(x):
            return 1 + 2 * x + 3 * x ** 2 + -(x / 2 - 1)

        p = 1 + 2 * X + 3 * X ** 2 + -(X / 2 - 1)
        self.assertEqual("1 + 2 * X + 3 * X ** 2 + -(X / 2 - 1)", str(p))
        for x in self.x:
            self.assertAlmostEqual(f(x), p(x))

        self.assertEqual(p, copy(p))
        self.assertFalse(p is copy(p))

        def f_(x):
            return 1/x - 2

        f = Curve(f_)
        g = 1 / (X + 2)

        self.assertEqual('f_', repr(f))
        for x in self.x:
            if not abs(x) == 2:
                self.assertAlmostEqual(f(g(x)), x)
                self.assertAlmostEqual(f(g)(x), x)
                self.assertAlmostEqual(g(f(x)), x)
                self.assertAlmostEqual(g(f)(x), x)

        h = Curve(1)
        self.assertEqual('1', repr(h))
        for x in self.x:
            self.assertAlmostEqual(f(g(h))(x), 1)
            self.assertAlmostEqual(g(h)(x), g(1))
