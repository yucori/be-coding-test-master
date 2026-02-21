from collections import deque

def solution(maze):

    def bfs(start, end):
        q = deque()
        q.append([start, [start]])
        paths = []
        
        while q:
            now, path = q.popleft()
            if end == now:
                paths.append(path)
                continue
            if len(path) > 16:
                continue
            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                current = [now[0] + move[0], now[1] + move[1]]
                if 0 <= current[0] < n and 0 <= current[1] < m:
                    if current not in walls and current not in path:
                        q.append([current, path+[current]])
        return paths

    n = len(maze)
    m = len(maze[0])
    walls = []

    for i in range(n):
        for j in range(m):
            check = maze[i][j]
            if check == 1:
                red_start = [i, j]
            elif check == 2:
                blue_start = [i, j]
            elif check == 3:
                red_end = [i, j]
            elif check == 4:
                blue_end = [i, j]
            elif check == 5:
                walls.append([i,j])

    answer = 17

    # 빨강과 파랑의 모든 경로를 BFS로 탐색해서 저장해둔다
    red_paths = bfs(red_start, red_end)
    blue_paths = bfs(blue_start, blue_end)

    if not red_paths or not blue_paths:
        return 0

    # 조건들을 비교
    for red_path in red_paths:
        for blue_path in blue_paths:
            if len(red_path) > len(blue_path):
                long_path = red_path
                short_path = blue_path
            else:
                long_path = blue_path
                short_path = red_path

            for lp in range(len(long_path) - 1):
                if lp < len(short_path)-1:
                    sp = lp
                else: 
                    sp = -1

                if long_path[lp] == short_path[sp]:
                    break

                if sp != -1:
                    if long_path[lp + 1] == short_path[sp] and long_path[lp] == short_path[sp+1]:
                        break
            # 정상적으로 for을 모두 통과한 경우에만 answer 갱신
            else:
                answer = min(answer, len(long_path)-1)
    return answer if answer != 17 else 0