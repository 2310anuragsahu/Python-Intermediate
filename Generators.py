def new(dict):
    for x, y in dict.items():
        yield x, y


a = {1: 'Hi', 2: 'Welcome'}

b = new(a)
print(b)
print(next(b))
print(next(b))

# -----------------using Yield twice with next()-----------------------------------
def ex():
    n = 3
    yield n
    n = n*n
    yield n


for x in ex():
    print(x)

# -------------------Generator expression---------------------------------
f = range(6)
print("List comprehension", end=":")
q = [x*2 for x in f]
print(q)

print("Generator expression", end=":")
r = (x*2 for x in f)
for x in r:
    print(x, end=", ")
