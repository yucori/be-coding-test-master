from itertools import combinations

def cal_min(ax, bx, ay, by):
  return abs(ax-bx)+abs(ay-by)

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input().split())))

ans = 999999999
chi = []
home = []

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      home.append((i, j))
    elif board[i][j] == 2:
      chi.append((i, j))
      
for ch in combinations(chi, m):
  temp = 0
  for h in home:
    chi_len = 999999
    for c in ch:
      chi_len = min(chi_len, cal_min(h[0], c[0], h[1], c[1]))
    temp += chi_len
  ans = min(ans, temp)

print(ans)