# Created by Akhitha Manjitha : 04.07.2022
import os
import mesh
from mesh import Mesh
import time


t = time.time()

input_files = os.path.join(
    os.path.dirname(mesh.__file__),
    "inputs"
)

sphere = Mesh()
sphere.read(os.path.join(input_files, "sphere.obj"))
cylinder = Mesh()
cylinder.read(os.path.join(input_files, "cylinder.obj"))

sphere.subset_intersecting_triangles(cylinder)
sphere.compact()
sphere.write(os.path.join(input_files, "sphere_out.obj"))

t2 = time.time() - t
print("Execution Time: ",  int(t2//60), "min :", t2 % 60, "seconds")






