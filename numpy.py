import numpy as np

#a1 = np.array([1,2,3])
#print(a1)

# a function that squares all the values
# in a sequence
def squares(values):
    result = []
    for v in values:
        result.append(v * v)
    return result


