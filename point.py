class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @staticmethod
    def dot(a, b):
        return a.x*b.x + a.y*b.y + a.z*b.z
    
    def normalize(self):
        length = (self.x**2 + self.y**2 + self.z**2)**0.5
        if length > 0:
            self.x /= length
            self.y /= length
            self.z /= length
    