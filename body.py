class Body:
    def __init__(self, mass, x, y, z, vx, vy, vz):
        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z

    def set_vx(self, vx):
        self.vx = vx

    def set_vy(self, vy):
        self.vy = vy

    def set_vz(self, vz):
        self.vz = vz

    def get_info(self):
        print(self.mass)
        print(self.x, self.y, self.z)
        print(self.vx, self.vy, self.vz)

Earth = Body(mass = 5.972e24, x = 0, y = 0, z = 0, vx = 0, vy = 0, vz = 0)
Earth.get_info()