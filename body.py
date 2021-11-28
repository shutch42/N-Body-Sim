class Body:
    def __init__(self, mass, x, y, z, vx, vy, vz):
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def get_info(self):
        print(self.mass)
        print(self.x, self.y, self.z)
        print(self.vx, self.vy, self.vz)
