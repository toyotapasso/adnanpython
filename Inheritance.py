class Shape():

    def Area(self,):
        area = 0


class Square(Shape):
    def __init__(self,length):
        self.length=length

    def Area(self,):
        area = self.length * self.length
        print("Area of Square = " + str(area))
sq = Square(3)
sq.Area()