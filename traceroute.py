"""Tracé de routes."""


from numpy import cos, sin, linspace, pi
import matplotlib.pyplot as plt


V = 1
u = 1


def rectd(f, a, b, n=1000):
    """Methode des rectangles à droite."""
    h, res = (b - a) / n, 0
    for i in range(1, n + 1):
        res += h * f(a + i * h)
    return res


def trapezes(f, a, b, n=1000):
    """Methode des trapezes."""
    h, res = (b - a) / n, 0
    for i in range(1, n+1):
        res += h*f(a+i*h) + (f(a+i*h)-f(a+(i-1)*h))*h/2
    return res


def mediane(f, a, b, n=1000):
    """Methode de la mediane."""
    h, res = (b - a) / n, 0
    for i in range(1, n+1):
        res += h*f(a + (2*i+1)/2*h)
    return res


def fx(t):
    return cos(t**2)


def fy(t):
    return sin(t**2)


def xrect(t):
    """Integral expression of x."""
    return V * rectd(fx, 0, t)


def yrect(t):
    """Integral expression of y."""
    return V * rectd(fy, 0, t)


def xmed(t):
    """Integral expression of x."""
    return V * mediane(fx, 0, t)


def ymed(t):
    """Integral expression of y."""
    return V * mediane(fy, 0, t)


def xtrap(t):
    """Integral expression of x."""
    return V * trapezes(fx, 0, t)


def ytrap(t):
    """Integral expression of y."""
    return V * trapezes(fy, 0, t)


xl = linspace(-3 * pi, 3 * pi, 10000)
yl = linspace(-3 * pi, 3 * pi, 10000)


plt.plot(xrect(xl), yrect(yl), label="Rectangles")
plt.plot(xmed(xl), ymed(yl), label="Mediane")
plt.plot(xtrap(xl), ytrap(yl), label="Trapezes")
plt.title("Integration numerique")
plt.legend()
plt.show()
