from collections import defaultdict

d = defaultdict(int)
d[1] = 'python'
d[2] = 'java'

print(d[3])

# Same program with regular dictionary will throw error
d1 = {1: 'python', 2: 'java'}
print(d1[3])
