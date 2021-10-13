import sys
sys.setrecursionlimit(100000)

n = int(input())

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if cabbage[x][y] == 1:
        cabbage[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
    return

for i in range(n):
    m, n, k = map(int, input().split())
    cabbage = [[0]*m for _ in range(n)]
    space = []
    cnt = 0
    for j in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
        space.append((y,x))
    while space:
        if cabbage[space[-1][0]][space[-1][1]] == 1:
            dfs(space[-1][0], space[-1][1])
            cnt += 1
        space.pop()
    print(cnt)
