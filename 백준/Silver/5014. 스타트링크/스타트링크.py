from collections import deque
F, S, G, U, D = map(int, input().split())

v = [0]*(F+1)

def bfs(idx):
  q = deque()
  q.append((idx, 0))
  v[idx] = True
  while q:
    cx, cnt = q.popleft()
    if cx == G:
      return cnt
    nx = cx + U
    if nx <= F and not v[nx]:
      v[nx] = True
      q.append((nx, cnt+1))
      
    nx = cx - D
    if nx >= 1 and not v[nx]:
      v[nx] = True
      q.append((nx, cnt+1))
        
  return("use the stairs")

print(bfs(S))
