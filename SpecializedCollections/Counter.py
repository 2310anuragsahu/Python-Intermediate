from collections import Counter

tempList = [1, 2, 1, 2, 1, 2, 3, 4, 5, 6, 7, 2, 1, 2]
count = Counter(tempList)
print(count)
print()

anotherList = list(count.elements())
print(anotherList);
print()

print(count.most_common())
print(count.most_common(2))
print()

sub = {2: 1, 6: 1}
count.subtract(sub)
print(count.most_common())
