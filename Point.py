
class Point:
    def __init__(self, x, y, srs):
        self.x = x
        self.y = y
        self.srs = srs

    def __str__(self) -> str:
        str = "Point ({0:.5f}, {1:.5f})".format(self.x, self.y)
        str += " EPSG code: {0}".format(self.srs)
        return str

    def distance_to(self, pt):
        return ((self.x - pt.x) ** 2 + (self.y - pt.x) ** 0.5)

    #kreirati klasu test_point.py

class Point3D(Point):
    def __init__(self, x, y, z, srs, units = "Meters"):
        Point.__init__(self, x, y, srs)
        self.z = z
        self.__units = units

    def __str__(self) -> str:
        str = "Point3D({0:.5f}, {1:.5f}, {2:.5f})".format(self.x, self.y, self.z)
        str += " EPSG code: {0}".format(self.srs)
        return str

    def distance_to(self, pt):
        return ((self.x - pt.x) ** 2 + (self.y - pt.y) ** 2) ** 0.5

    def distance3D_to(self, pt):
        return ((self.x - pt.x) ** 2 + (self.y - pt.y) ** 2 + (self.z - pt.z) ** 2) ** 0.5

    def get_units(self):
        return self.__units

    def set_units(self, units):
        if units in ["Meters", "Feet"]:
            self.__units = units
        else:
            print("{0} is not a valid unit for elavation".format(units))
