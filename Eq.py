class A():
    def __eq__(self, other):
        print("A __eq__ called")
      #  print(other)
        return self.value == other
#class B(object):
 #   def __eq__(self, other):
 #       print("B __eq__ called")
 #       print(other)
 #       return self.value == other

a = A()
a.value = 3
b = A()
b.value = 4
print(a == b)
