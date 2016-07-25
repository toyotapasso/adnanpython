x=3
y=5

array = []

for i in range(0,x):
    array.append([])
    for j in range (0,y):
        array[i].append(i*j)
print(array)