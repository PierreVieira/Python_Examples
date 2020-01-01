from functools import reduce
#Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#Using reduce
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))
#Using loop
product = 1
for x in data:
    product *= x
print(product)
