# -*- coding: utf-8 -*-

# curves
# ------
# functional curve algebra (created by auxilium)
#
# Author:   sonntagsgesicht
# Version:  0.1.4, copyright Friday, 11 October 2024
# Website:  https://github.com/sonntagsgesicht/curves
# License:  Apache License 2.0 (see LICENSE file)


TOL = 1e-8
MAX_ITER = 1_000
EPS = 1e-7


def finite_difference(f, x, h=EPS):
    """
    Numerically differentiate the function f at point x
    using the finite difference method.


    :param f: (function) The function to differentiate.
    :param x: (float) The point at which to differentiate the function.
    :param h: (float, optional) The step size to use. Default is 1e-7.

    :return: float: The numerical derivative of f at point x.
    """
    return (f(x + h) - f(x - h)) / (2 * h)


def trapezoidal_rule(f, a, b, n):
    """
    Numerically integrate the function f from a to b
    using the trapezoidal rule with n intervals.

    :param f: (function) The function to integrate.
    :param a: (float) The start point of the interval.
    :param b: (float) The end point of the interval.
    :param n: (int) The number of intervals to divide [a, b] into.

    :return: float: The numerical integral of f from a to b.
    """
    # Calculate the width of each interval
    h = (b - a) / n

    # Calculate the sum of f(x) for each interval
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)

    # Multiply by the width of the intervals
    integral *= h

    return integral


def quadrature(f, a, b):
    """
    Numerically integrate the function f from a to b
    using the quadrature rule.

    :param f: (function) The function to integrate.
    :param a: (float) The start point of the interval.
    :param b: (float) The end point of the interval.

    :return: float: The numerical integral of f from a to b.
    """
    nodes = {0.0: 0.20948214108472782,
             -0.20778495500789848: 0.20443294007529889,
             0.20778495500789848: 0.20443294007529889,
             -0.4058451513773972: 0.19035057806478542,
             0.4058451513773972: 0.19035057806478542,
             -0.5860872354676911: 0.1690047266392679,
             0.5860872354676911: 0.1690047266392679,
             -0.7415311855993945: 0.14065325971552592,
             0.7415311855993945: 0.14065325971552592,
             -0.8648644233597691: 0.10479001032225019,
             0.8648644233597691: 0.10479001032225019,
             -0.9491079123427585: 0.06309209262997856,
             0.9491079123427585: 0.06309209262997856,
             -0.9914553711208126: 0.022935322010529224,
             0.9914553711208126: 0.022935322010529224}
    m = 0.5 * (b + a)
    h = 0.5 * (b - a)
    return sum(w * f(m + h * n) for n, w in nodes.items()) * h


integrate = quadrature


def newton_raphson(f, a, tol=TOL, max_iter=MAX_ITER):
    """
    Newton-Raphson method to find the root of a function.

    :param f: (callable) function
    :param a: (float) Initial guess
    :param tol: (float) Tolerance for convergence
    :param max_iter: (int) Maximum number of iterations

    :return: float : The root of the function
    """
    for i in range(max_iter):
        fa = f(a)
        dfa = finite_difference(f, a)
        if dfa == 0:
            raise ZeroDivisionError("Derivative is zero at {a=}")

        b = a - fa / dfa

        # Check for convergence
        if abs(b - a) < tol:
            return b

        a = b

    raise RuntimeError("Exceeded maximum iterations")


def bisection_method(f, a, b, tol=TOL, max_iter=MAX_ITER):
    """
    Bisection method to find the root of a function.

    :param f: (callable) function
    :param a: (float) Left endpoint of the initial interval
    :param b: (float) Right endpoint of the initial interval
    :param tol: (float) Tolerance for convergence
    :param max_iter: (int) Maximum number of iterations

    :return: float : The root of the function
    """
    if f(a) * f(b) >= 0:
        msg = f"The function must have opposite signs at {a=} and {b=}"
        raise ValueError(msg)

    for _ in range(max_iter):
        # Calculate midpoint
        c = (a + b) / 2

        # Check if midpoint is a root
        # or if the interval is smaller than tolerance
        if abs(f(c)) < tol or abs(b - a) / 2 < tol:
            return c

        # Decide the side to repeat the steps on
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    raise RuntimeError("Exceeded maximum iterations")


def secant_method(f, a, b, tol=TOL, max_iter=MAX_ITER):
    """
    Secant method to find the root of a function.

    :param f: (callable) function
    :param a: (float) First initial guess
    :param b: (float) Second initial guess
    :param tol: (float) Tolerance for convergence
    :param max_iter: (int) Maximum number of iterations

    :return: float : The root of the function
    """
    for i in range(max_iter):
        # Calculate the value of the function at the initial guesses
        fa = f(a)
        fb = f(b)

        if abs(fb - fa) < tol:
            msg = f"Denominator is too small at {a=} and {b=}"
            raise ZeroDivisionError(msg)

        # Compute the next approximation
        c = b - fb * (b - a) / (fb - fa)

        # Check for convergence
        if abs(c - b) < tol:
            return c

        # Update guesses
        a, b = b, c

    raise RuntimeError("Exceeded maximum iterations")


def solve(f, method='secant_method', *args, **kwargs):
    """solver providing function

    :param f: (callable) function
    :param method: (str or callable) solver method
    :param args: **method** arguments
    :param kwargs: **method** keyword arguments
    :return:

    """
    if callable(method):
        return method(f, *args, **kwargs)

    # default method
    method = str(method) if method else 'secant_method'

    # gather arguments
    guess = kwargs.get('guess', None)
    a, b = kwargs.pop('bounds', (guess, None))
    a = kwargs.pop('a', a)
    b = kwargs.pop('b', b)
    if a:
        kwargs['a'] = a
    if b:
        kwargs['b'] = b

    tol = kwargs.pop('tol', None)
    tol = kwargs.pop('tolerance', tol)
    tol = kwargs.pop('precision', tol)
    if tol:
        kwargs['tol'] = tol

    if 'newton' in method:
        if len(args) < 1:
            kwargs['a'] = kwargs.get('a', 0.01)
        return newton_raphson(f, *args, **kwargs)

    if 'secant' in method:
        if len(args) < 1:
            kwargs['a'] = kwargs.get('a', 0.01)
        if len(args) < 2:
            kwargs['b'] = kwargs.get('b', 0.1)
        return secant_method(f, *args, **kwargs)

    if 'bisec' in method:
        if len(args) < 1:
            kwargs['a'] = kwargs.get('a', -0.1)
        if len(args) < 2:
            kwargs['b'] = kwargs.get('b', 0.2)
        return bisection_method(f, *args, **kwargs)

    raise ValueError(f"unknown method {method}")


# Example usage integration
if __name__ == "__main__":
    from math import exp, pi
    from scipy.integrate import quad as _scipy_quad

    f = (lambda x: exp(-x ** 2))
    a = 0.0
    b = 1.0
    n = 7

    print(f"quadrature:         {quadrature(f, a, b)}")
    print(f"scipy:              {_scipy_quad(f, a, b)[0]}")
    print(f"trapezoidal_rule:   {trapezoidal_rule(f, a, b, 1000)}")


# Example usage differentiation
if __name__ == "__main__":

    # Differentiate func at x = π/4
    f = exp
    x_point = pi / 4
    a, b = -1, pi

    derivative = finite_difference(f, x_point)
    print("Derivative at x =", x_point, "is", derivative)

    # Integrate func from 0 to π with 1000 intervals
    result = trapezoidal_rule(f, a, b, 1000)
    print("Integral trapezoidal_rule result:", result)

    # Integrate func from 0 to π with 1000 intervals
    result = quadrature(f, a, b)
    print("Integral quadrature result:      ", result)

    # Integrate func from 0 to π with 1000 intervals
    result = _scipy_quad(f, a, b)[0]
    print("Integral scipy result:           ", result)


# Example usage root finding
if __name__ == "__main__":
    def f(x):
        # f(x) = x^2 - 2
        return x ** 2 - 2

    print(f"newton_raphson: {newton_raphson(f, 1.0)}")
    print(f"bisection_method: {bisection_method(f, -1.0, 2.0)}")
    print(f"secant_method: {secant_method(f, 1.0, 2.0)}")

    def f(x):
        return exp(x) - 3.

    print(f"newton_raphson: {newton_raphson(f, 1.0)}")
    print(f"bisection_method: {bisection_method(f, -1.0, 2.0)}")
    print(f"secant_method: {secant_method(f, 1.0, 2.0)}")
