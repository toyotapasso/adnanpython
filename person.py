class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

#    def displayinfo(self):
 #       print("name =" + self.name)
  #      print("age = "+ str(self.age))

    def __str__(self):
        print(self.name)
        print(self.age)
        str1 = self.name + " " + str(self.age)
        return str1

p = Person("adnan",35)
#p.displayinfo()
print(p)