from collections import ChainMap

d1 = {1: 'A', 2: 'B'}
d2 = {3: 'C', 4: 'D'}

d = ChainMap(d1, d2)
print(d)

print(d.get(3))
print(d.get(1))
print(d.__len__())
