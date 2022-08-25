# Created by Akhitha Manjitha : 04.07.2022
from typing import List
import edge
from point import Point
from vector import Vector


class Triangle:
    """3D triangle made up of three points out of a global points list"""

    def __init__(self, points: List[Point], a: int, b: int, c: int):
        self._points = points
        self.a = a - 1
        self.b = b - 1
        self.c = c - 1

    def edges(self) -> List[edge.Edge]:
        """Returns the list of edges in the triangle"""
        e1 = edge.Edge(self._points, self.a, self.b)
        e2 = edge.Edge(self._points, self.b, self.c)
        e3 = edge.Edge(self._points, self.a, self.c)
        edge_list  = [e1, e2, e3]
        return edge_list

    def centre(self) -> Point:
        """Returns the triangle centre"""
        p1 = self._points[self.a]
        p2 = self._points[self.b]
        p3 = self._points[self.c]

        x = (p1.x() + p2.x() + p3.x())/3.0
        y = (p1.y() + p2.y() + p3.y())/3.0
        z = (p1.z() + p2.z() + p3.z())/3.0

        return Point(x,y,z)



    def area(self) -> float:
        """Returns the triangle area"""
        vec1 = self._points[self.b].__sub__(self._points[self.a])
        vec2 = self._points[self.c].__sub__(self._points[self.a])

        cross_vec = vec1.cross(vec2)
        area = cross_vec.norm() / 2.0
        return area

    def normal(self) -> Vector:
        """
        Returns the triangle normal vector. Does not need to be normalised
        """
        vec1 = self._points[self.b].__sub__(self._points[self.a])
        vec2 = self._points[self.c].__sub__(self._points[self.a])

        return vec1.cross(vec2)

    def inside(self, p: Point) -> bool:
        """Returns true if the normal projection of the point is inside the triangle"""
        vec_ap = p.__sub__(self._points[self.a])
        proj = self.normal().__mul__((vec_ap.dot(self.normal()) / (self.normal().norm() ** 2)))
        point_vec = p.__sub__(proj)
        point = Point(point_vec._v[0], point_vec._v[1], point_vec._v[2])

        points_lis = [self._points[self.a], self._points[self.b], self._points[self.c], point]

        tr1 = Triangle(points_lis, 1,2,4)
        tr2 = Triangle(points_lis, 1,3,4)
        tr3 = Triangle(points_lis, 2,3,4)

        total_area = tr1.area() + tr2.area() + tr3.area()

        if(total_area > self.area()):
            return False
        else:
            return True


