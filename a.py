a = [3, 1, 365, 2, 6, 2, 6, 9]
b = list(a)
print(a, b)
print(id(a), id(b))
print(a[0], b[0])
print(id(a[0]), id(b[0]))
b.pop([0:4])
print(a, b)
print(id(a), id(b))
