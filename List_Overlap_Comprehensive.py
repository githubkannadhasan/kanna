import random

list1 = random.sample(range(30), 8)
list2 = random.sample(range(20), 12)

# Convert it as array

array1 = set(list1)
array2 = set(list2)

common = array1.intersection(array2)

print( array1)
print(array2)
print( common)

