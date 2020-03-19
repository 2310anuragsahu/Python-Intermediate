from collections import deque

tempList = ['a', 'b', 'c', 'd', 'e', 'f']
d = deque(tempList)
print(d)

d1 = d.copy()
print(d1.clear())

d.append('x')
d.appendleft('z')
print(d)

d.pop()
d.popleft()
print(d)

d.reverse()
print(d)
