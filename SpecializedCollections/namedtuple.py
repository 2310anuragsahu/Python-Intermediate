from collections import namedtuple

details = namedtuple('courses', 'name, technology')
anurag = details('Machine Learning', 'Python')
print(anurag)
print(anurag.__getattribute__('technology'))

print()

dave = details._make(['AI', 'Python + Selenium'])
print(dave)
print(dave.__getitem__(0))
