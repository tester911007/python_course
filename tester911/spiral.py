n = int(input())

matrix = [[0 for i in range(n)] for j in range(n)]

y, x = 0, 0
step = 0
limit = n - 1
for i in range(1, n ** 2 + 1):
    matrix[y][x] = i

    if x < limit:
        x += 1
    elif y < limit:
        y += 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
