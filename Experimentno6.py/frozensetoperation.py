a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)
print("Is Subset:", a.issubset(b))
print("Is Superset:", a.issuperset(b))
print("Is Disjoint:", a.isdisjoint(b))

