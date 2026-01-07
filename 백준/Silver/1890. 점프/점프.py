# 백준 1890

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * n for _ in range(n)]
v[0][0] = 1

for i in range(n):
    for j in range(n):
        if v[i][j] == 0 or (i == n-1 and j == n-1):
            continue
        dis = board[i][j]
        if i + dis < n:
            v[i + dis][j] += v[i][j]
        if j + dis < n:
            v[i][j + dis] += v[i][j]

print(v[n - 1][n - 1])