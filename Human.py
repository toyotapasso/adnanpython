class Human():
    def method(self):
        print("parent method")

class Person(Human):
    def method(self):
        print("Child method")
        super(Person,self).method()

p = Person()
p.method()