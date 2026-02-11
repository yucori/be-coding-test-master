from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    # 각 열마다 얻을 수 있는 총 석유량을 저장할 배열
    result = [0] * m
    # 방문 여부 체크
    visited = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # 석유가 있고 아직 방문하지 않은 곳이라면 BFS 시작
            if land[i][j] == 1 and not visited[i][j]:
                # 1. BFS로 석유 덩어리 탐색
                q = deque([(i, j)])
                visited[i][j] = True
                
                count = 0        # 현재 덩어리의 석유량
                
                # 덩어리가 포함된 열들을 중복 없이 저장하기 위한 set
                cols = set()
                
                while q:
                    r, c = q.popleft()
                    count += 1
                    cols.add(c) # 시추관이 통과하는 열 저장
                    
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        
                        # 범위 내에 있고, 석유이며, 방문하지 않은 경우
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                
                # 2. 탐색이 끝난 후, 해당 덩어리가 속한 모든 열에 석유량 합산
                for col in cols:
                    result[col] += count
    
    # 3. 모든 열 중 가장 많은 석유량 반환
    return max(result)

# def solution(land):
#     lenx = len(land[0])
#     leny = len(land)
#     ans = [0]*lenx
#     visited = [[False]*lenx for _ in range(leny)]
    
#     for i in range(lenx):
#         for j in range(leny):
#             if land[i][j] == 1 and visited[i][j] != False:
#                 q = deque([i, j])
#                 visited[i][j] = True
#                 cnt = 0
#                 xs = set()
                
#                 while q:
#                     x, y = q.popleft()
#                     cnt += 1
#                     xs.add(x)
#                     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                         cx, cy = x+dx, y+dy
                        
#                         if 0<=cx<lenx and 0<=cy<leny:
#                             if land[cx][cy] == 1 and not visited[cx][cy]:
#                                 visited[cx][cy] = True
#                                 q.append((cx, cy))
#                 for col in xs:
#                     ans[col] += cnt
    
#     return max(ans)