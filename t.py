def gtlrm(isStr = True, number = 0):
    if isStr:
        for i in range(rows):
            print(number, i)
    else:
        for i in range(strings):
            print(i, rows)
strings, rows = [int(x) for x in input().split()]
mat = []
for i in range(strings):
    mat.append([int(x) for x in input().split()])
print(mat)
del mat[0:1][2:2]
print(mat)
