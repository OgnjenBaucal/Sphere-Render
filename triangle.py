from point import Point

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    
    def normal(self):
        AB = Point(self.B.x - self.A.x, self.B.y - self.A.y, self.B.z - self.A.z)
        AC = Point(self.C.x - self.A.x, self.C.y - self.A.y, self.C.z - self.A.z)
        
        # Cross product AB x AC
        N_x = AB.y * AC.z - AB.z * AC.y
        N_y = AB.z * AC.x - AB.x * AC.z
        N_z = AB.x * AC.y - AB.y * AC.x
        
        normal = Point(N_x, N_y, N_z)
        normal.normalize()

        return normal

    def centroid(self):
        x = self.A.x + self.B.x + self.C.x / 3
        y = self.A.y + self.B.y + self.C.y / 3
        z = self.A.z + self.B.z + self.C.z / 3
        return Point(x, y, z)
