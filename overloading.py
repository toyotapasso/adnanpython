class A:
    def stackoverflow(self,i,j):
        print("first method")
    def stackoverflow(self, i):
        print("second method," + str(i))


ob=A()
ob.stackoverflow(2,3)