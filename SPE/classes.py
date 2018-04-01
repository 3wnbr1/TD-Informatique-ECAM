#! /Users/ewen/anaconda3/bin/python
# coding: utf-8


"""Classes Point, Vecteur, Torseurs."""


import pdb
import numpy as np


class Point:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def vectorize(self):
        return Vector(self._x, self._y, self._z)

    def __add__(self, point):
        return Point(self._x + point._x, self._y + point._y, self._z + point._z)

    def __sub__(self, point):
        return Point(self._x - point._x, self._y - point._y, self._z - point._z)

    def __str__(self):
        return "(%d, %d, %d)" % (self._x, self._y, self._z)

    def __repr__(self):
        return "<Point (%d, %d, %d)>" % (self._x, self._y, self._z)


class Vector:
    """Vector Class."""
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def norm(self):
        return (self._x**2+self._y**2+self._z**2)**(1/2)

    def dot_product(self, vector):
        assert isinstance(vector, Vector), "NOT A VECTOR"
        return self._x*vector._x + self._y*vector._y + self._z*vector._z

    def cross_product(self, vector):
        assert isinstance(vector, Vector), "NOT A VECTOR"
        x = self._y*vector._z - self._z*vector._y
        y = self._z*vector._x - self._x*vector._z
        z = self._x*vector._y - self._y*vector._x
        return Vector(x, y, z)

    def cylindrical(self):
        r = (self._x**2 + self._y**2)**1/2
        return (r, np.arccos(self._x/r), self._z)

    def __add__(self, vector):
        assert isinstance(vector, Vector), "NOT A VECTOR"
        return Vector(self._x + vector._x, self._y + vector._y, self._z + vector._z)

    def __str__(self):
        return "(%d, %d, %d)" % (self._x, self._y, self._z)

    def __repr__(self):
        return "<Vector (%d, %d, %d)>" % (self._x, self._y, self._z)


class Torsor:
    def __init__(self, r=Vector(), m=Vector(), point=Point()):
        assert isinstance(point, Point), "NOT A POINT"
        assert isinstance(r, Vector) and isinstance(m, Vector), "NOT VECTORS"
        self._r = r
        self._m = m
        self._point = point

    @property
    def point(self):
        return self._point

    @point.setter
    def point(self, point):
        assert isinstance(point, Point), "NOT A POINT"
        self._m = self._m + (self.point - point).vectorize().cross_product(self._r)
        self._point = point

    def comoment(self, torsor):
        assert isinstance(torsor, Torsor), "NOT A TORSOR"
        return self._r.dot_product(torsor._m) + self._m.dot_product(torsor._r)

    def __add__(self, torsor):
        assert isinstance(torsor, Torsor), "NOT A TORSOR"
        torsor.point = self.point
        return Torsor(self._r + torsor._r, self._m + torsor._m, self.point)

    def __str__(self):
        return "{ %d  , %d\n  %d  , %d\n  %d , %d }" % (self._r._x, self._m._x, self._r._y, self._m._y, self._r._z, self._m._z)

    def __repr__(self):
        return "<Torsor>\n{ %d  , %d\n  %d  , %d\n  %d , %d }\n" % (self._r._x, self._m._x, self._r._y, self._m._y, self._r._z, self._m._z) + "@Point" + self._point.__str__()


if __name__ == '__main__':
    vector = Vector(1, 2, 3)
