
from .numerics import finite_difference, quadrature, EPS


class Integral:

    def __init__(self, curve, a=0):
        self.curve = curve
        self.a = a

    def __call__(self, x):
        return quadrature(self.curve, self.a, x)

    def __getitem__(self, item):
        return self.__class__(self.curve, item)

    def __repr__(self):
        _ = f", {self.a}" if self.a else ''
        return f"{self.__class__.__name__}({self.curve}{_})"


class Derivative:

    def __init__(self, curve, h=EPS):
        self.curve = curve
        self.h = h

    def __call__(self, x):
        return finite_difference(self.curve, x, self.h)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.curve})"
