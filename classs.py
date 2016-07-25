class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        area = 3.142 * self.radius**2
        print("Area = "+str(area))

cir = Circle(2)
cir.Area()