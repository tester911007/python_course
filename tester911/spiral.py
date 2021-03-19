# put your python code here
n = int(input())

matrix = [[0 for i in range(n)] for j in range(n)]

y, x = 0, 0
step = 0
limit = n - 1
step = 0
for i in range(1, n ** 2 + 1):
    matrix[y][x] = i

    if step % 2 == 0:
        if x < limit:
            x += 1
        elif y < limit:
            y += 1
        else:
            step = 1
            x -= 1
    elif step % 2 == 1:
        if x > (n - limit - 1):
            x -= 1
        elif y > (n - limit):
            y -= 1
        else:
            step = 2
            limit -= 1
            x += 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
