count = 0
for x in range(2000, 3200) :
  if x%7 == 0 and x%5 !=0 :
      print(str(x) + ',')
      count=count+1
print("Total Values = " + str(count))
