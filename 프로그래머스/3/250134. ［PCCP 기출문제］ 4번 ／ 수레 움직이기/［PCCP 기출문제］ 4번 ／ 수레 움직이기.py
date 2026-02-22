from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red_start = (i, j)
            elif maze[i][j]  == 2: blue_start = (i, j)
            elif maze[i][j] == 3: red_end = (i, j)
            elif maze[i][j] == 4: blue_end = (i, j)

    q = deque([(red_start, blue_start, {red_start}, {blue_start}, 0)])

    while q:
        r_now, b_now, r_visited, b_visited, cnt = q.popleft()

        if r_now == red_end and b_now == blue_end:
            return cnt

        r_candidates = [r_now] if r_now == red_end else []
        if not r_candidates:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r_now[0] + dx, r_now[1] + dy
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5 and (nr, nc) not in r_visited:
                    r_candidates.append((nr, nc))

        b_candidates = [b_now] if b_now == blue_end else []
        if not b_candidates:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = b_now[0] + dx, b_now[1] + dy
                if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] != 5 and (nr, nc) not in b_visited:
                    b_candidates.append((nr, nc))
                    
        for r_next in r_candidates:
            for b_next in b_candidates:
                if r_next == b_next: continue
                if r_next == b_now and b_next == r_now: continue
                
                new_r_v = r_visited | {r_next}
                new_b_v = b_visited | {b_next}
                
                q.append((r_next, b_next, new_r_v, new_b_v, cnt+1))
    return 0