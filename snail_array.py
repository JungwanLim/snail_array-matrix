def snail_array(size, arr):
    x, y = -1, 0
    n, increase = 1, 1
    for j in range(size, 0, -1):
        for i in range(1, j * 2):
            if i <= j:
                x += increase
            else:
                y += increase
            arr[y][x] = n
            n += 1
        increase *= (-1)
n = 7
arr = [[0] * n for i in range(n)]
snail_array(n, arr)
for i in range(n):
    for j in range(n):
        print("%2d" %arr[i][j], end = ' ')
    print()
    
print()
print("=" * 30)
def snail_array(x, y, size, increase, n, arr):
    if size <= 0:
        return
    for i in range(1, size * 2):
        if i <= size:
            x += increase
        else:
            y += increase
        arr[y][x] = n
        n -= 1
    snail_array(x, y, size - 1, -increase, n, arr)
snail_array(-1, 0, n, 1, n * n, arr)
for i in range(n):
    for j in range(n):
        print("%2d" %arr[i][j], end = ' ')
    print()
