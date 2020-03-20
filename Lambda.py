list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double = list(map(lambda x: x*2, list1))
print(double)
print()

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_multipleOf_3 = list(filter(lambda a: (a % 3 == 0), list2))
print(list_multipleOf_3)
print()

from functools import reduce
r = reduce(lambda a,b: a + b, [1, 2, 3, 4, 5])
print(r)
print(8)

# Using filter, map and reduce all at once
result = reduce(lambda x, y: (x+y), map(lambda x: (x/2), filter(lambda x: (x % 2 == 0), [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(result)
