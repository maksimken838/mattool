s = 0
n = 10
a = [0, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
for i in range(1, 11):
    if i == n - i:
        s = s + a[i] + a[i + 1]
print(s)
