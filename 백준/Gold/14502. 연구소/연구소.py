from itertools import combinations
from collections import deque
import copy

def bfs(a, b, d_board, virus):
  q = deque()
  for i, j in virus:
    q.append((i, j))
        
  while q:
    x, y = q.popleft()
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      nx, ny = x+dx, y+dy
      
      if not(0<=nx<a and 0<=ny<b):
        continue
        
      if d_board[nx][ny] == 0:
        d_board[nx][ny] = 2
        q.append((nx, ny))
            

n, m = map(int, input().split())
board = []
ans = 0
for _ in range(n):
  board.append(list(map(int, input().split())))

arr0 = []
arr2 = []

for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      arr0.append((i, j))
    elif board[i][j] == 2:
      arr2.append((i, j))
    
      
for t_w in combinations(arr0, 3):
  t_board = copy.deepcopy(board)
  for x, y in t_w:
    t_board[x][y] = 1
  
  bfs(n, m, t_board, arr2)
  safe = sum(row.count(0) for row in t_board)
  ans = max(ans, safe)

print(ans)