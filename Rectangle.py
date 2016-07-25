class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width=width

    def Area(self):
        area = self.length*self.width
        print("Area of Rectangle = "+str(area))

rec = Rectangle(2,2)
rec.Area()