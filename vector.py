# Created by Akhitha Manjitha : 04.07.2022
class Vector(object):
    """3D vector implementation"""

    def __init__(self, v: tuple([float, float, float])):
        self._v = v

    def __add__(self, v: "Vector") -> "Vector":
        """Adds two vectors"""
        ret =  tuple([self._v[0] + v._v[0], self._v[1] + v._v[1], self._v[2] + v._v[2]])
        return Vector(ret)

    def __sub__(self, v: "Vector") -> "Vector":
        """Subtracts two vectors"""
        ret = tuple([self._v[0] - v._v[0], self._v[1] - v._v[1], self._v[2] - v._v[2]])
        return Vector(ret)

    def __mul__(self, f: float) -> "Vector":
        """Multiplies vector by given scalar f"""
        ret = tuple([self._v[0] * f, self._v[1] * f, self._v[2] * f])
        return Vector(ret)

    def __truediv__(self, f: float) -> "Vector":
        """Divides vector by given scalar f"""
        ret = tuple([self._v[0] / f, self._v[1] / f, self._v[2] / f])
        return Vector(ret)

    def norm(self) -> float:
        """Returns the vector norm"""
        return (self._v[0] ** 2 + self._v[1] ** 2 + self._v[2] ** 2) ** (1/2)

    def dot(self, v: "Vector") -> float:
        """Returns the dot product between the two vectors"""
        return (self._v[0] * v._v[0] + self._v[1] * v._v[1] + self._v[2] * v._v[2])

    def cross(self, v: "Vector") -> "Vector":
        """Returns the cross product between the two vectors"""
        ret = tuple([self._v[1] * v._v[2] - self._v[2] * v._v[1], self._v[2] * v._v[0] - self._v[0] * v._v[2], self._v[0] * v._v[1] - self._v[1] * v._v[0]])
        return Vector(ret)

    def normalise(self):
        """Normalises the vector in-place"""
        return self.__truediv__(self.norm())
