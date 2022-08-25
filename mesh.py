# Created by Akhitha Manjitha : 04.07.2022
from point import Point
from triangle import Triangle


class Mesh:

    def __init__(self):
        self.points: list[Point] = []
        self.triangles: list[Triangle] = []

    def read(self, file: str):
        """
        Reads mesh from file. The file format supports two element types: a point and a triangle
        Each line represents a single mesh element.

        A point can be assumed to be represented as follows:
            v <float> <float> <float>
        For example:
            v 0.2 0.4 0.35

        A triangle can be assumed to be represented as follows:
            f <int> <int> <int>
        For example:
            f 5 199 86
        Where the integer indices to points in the global points list (the triangle above is thus formed of points 5,
        199 and 86 (in that order) from the global points list

        There is no guarantee that all points are specified before all faces.
        However, it can be assumed that at the point any single face is read in, the relevant points have already been
        defined
        """

        lines = open(file, 'r').readlines()
        for line in lines:
            if(line[0] == 'v' or line[0] == 'V'):
                line = line.replace('\n', '')
                line = line.split(' ')[1:]
                line = [float(i) for i in line]
                point = Point(x = line[0], y = line[1], z = line[2])
                self.points.append(point)
            if(line[0] == 'f' or line[0] == 'F'):
                line = line.replace('\n', '')
                line = line.split(' ')[1:]
                line = [int(i) for i in line if i not in ['', ' ']]
                triangle = Triangle(points=self.points, a=line[0], b=line[1], c=line[2])
                self.triangles.append(triangle)


    def write(self, file: str):
        """
        Writes the mesh to the specified file in the same format as specified in the read function above
        """
        obj_str = ""
        for point in self.points:
            obj_str += "v " + str(point.x()) + " " + str(point.y()) + " " + str(point.z()) + " \n"
        for triangle in self.triangles:
            obj_str += 'f ' + str(triangle.a + 1) + " " + str(triangle.b + 1) + " " + str(triangle.c + 1) + "\n"
        
        f = open(file, 'w+')
        f.write(obj_str)
        f.close()


    def subset_intersecting_triangles(self, other: "Mesh"):
        """
        Removes all triangles from this mesh, except for those which contain at least one edge which intersects the
        other mesh
        """
        new_triangles = []
        for triangle in self.triangles:
            edges = triangle.edges()
            for edge in edges:
                for tri in other.triangles:
                    if(edge.intersects(tri)):
                        new_triangles.append(triangle)
                        break
        self.triangles = new_triangles        


    def compact(self):
        """
        Removes all points which are not used by any triangle, thus reducing the resultant file size
        Note that as the points list changes in size, the triangles need to be updated to correctly reflect the new
        points list
        """
        point_indexes = []
        for triangle in self.triangles:
            a = triangle.a
            b = triangle.b
            c = triangle.c
            lis = [a,b,c]

            for i in lis:
                if(i not in point_indexes):
                    point_indexes.append(i)
        point_indexes.sort()
            
        new_points = []
        count = 0
        for i in point_indexes:
            new_points.append(self.points[i])
            for triangle in self.triangles:
                if(triangle.a == i):
                    triangle.a = count
                elif(triangle.b == i):
                    triangle.b = count
                elif(triangle.c == i):
                    triangle.c = count
            count += 1
        
        self.points = new_points
#-------------------------------------------------
        # new_points = []
        # new_triangles = []

        # for triangle in self.triangles:
        #     p1 = self.points[triangle.a]
        #     p2 = self.points[triangle.b]
        #     p3 = self.points[triangle.c]

        #     lis = [p1, p2, p3]

        #     for point in lis:
        #         if(point not in new_points):
        #             new_points.append(point)


        #     triangle.a = new_points.index(p1)
        #     triangle.b = new_points.index(p2)
        #     triangle.c = new_points.index(p3)
        
        # self.points = new_points
        #------------------------------------------------

        # new_points = []
        # for i in range(len(self.points)):
        #     for triangle in self.triangles:
        #         a = triangle.a
        #         b = triangle.b
        #         c = triangle.c

        #         lis = [a,b,c]

        #         for j  in lis:
        #             if(i == j):
                        

        #         if(a == i):
        #             if (self.points[i] not in new_points):
        #                 new_points.append(self.points[i])

            




            

