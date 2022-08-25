# Created by Akhitha Manjitha : 04.07.2022
from vector import Vector


class Point(Vector):
    """Vector implementation representing point in space"""

    def __init__(self, x: float, y: float, z: float):
        super(Point, self).__init__((x, y, z))

    def x(self):
        return self._v[0]

    def y(self):
        return self._v[1]

    def z(self):
        return self._v[2]

