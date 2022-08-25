# Created by Akhitha Manjitha : 04.07.2022

from point import Point
from typing import List
import triangle



class Edge:
    """3D edge made up of two points out of a global points list"""

    def __init__(self, points: List[Point], a: int, b: int):
        self._points = points
        self.a = a
        self.b = b

    def intersects(self, t: "triangle.Triangle") -> bool:
        """Returns true if the edge intersects the provided triangle"""
        
        p = self._points[self.a]
        q = self._points[self.b]
        c = t.centre()
        n = t.normal()

        numerator = (n._v[0] * (c.x() - p.x())) + (n._v[1] * (c.y() - p.y())) + (n._v[2] * (c.z() - p.z()))
        denominator = (n._v[0] * (q.x() - p.x())) + (n._v[1] * (q.y() - p.y())) + (n._v[2] * (q.z() - p.z()))

        if(numerator == 0 and denominator == 0):
            return True
        elif(numerator != 0 and denominator == 0):
            return False
        else:
            val = numerator / denominator
            x = p.x() + val * (q.x() - p.x())
            y = p.y() + val * (q.y() - p.y())
            z = p.z() + val * (q.z() - p.z())
            point = Point(x, y, z)

            edge_dist = (q.__sub__(p)).norm()
            dist1 = (point.__sub__(p)).norm()
            dist2 = (q.__sub__(point)).norm()

            if(edge_dist < dist1 + dist2):
                return False
            else:
                if(t.inside(point)):
                    return True
                else:
                    return False
            

            