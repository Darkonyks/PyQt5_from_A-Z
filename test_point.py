import Point as pt 

pt1 = pt.Point(3, 12, 4326)
#dodavanje 3D distance i tacke
pt3 = pt.Point3D(3, 12, 2000, 4326)
pt2 = pt.Point3D(6, 16, 2200, 4326, "Feet")

print(pt1.srs)
print(pt1.distance_to(pt2))
print(pt2.distance_to(pt3))
print(pt2.distance3D_to(pt3))
print(pt1)
print(pt2)
print(type(pt1))
print(type(pt2))
pt2.set_units("Cubits")
print(pt2.get_units())