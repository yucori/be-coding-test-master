def solution(points, routes):
    answer = 0
    x = len(routes)
    moving = [[] for _ in range(x)]
    
    # 로봇 각자의 이동 경로들을 다 저장해둠 - 리스트로
    
    for i in range(x):
        idx_from = routes[i][0] - 1
        cx, cy = points[idx_from]
        
        moving[i].append((cx, cy))
        
        for j in range(1, len(routes[i])):
            idx_to = routes[i][j] - 1
            dx, dy = points[idx_to]
            
            while cx != dx:
                cx += 1 if cx < dx else -1
                moving[i].append((cx, cy))
            
            while cy != dy:
                cy += 1 if cy < dy else -1
                moving[i].append((cx, cy))
    
    # 그 경로들을 가면서 충돌 횟수 count하여 ans+=cnt. 목적지 도달 시 x--
    
    max_len = max(len(path) for path in moving)
    
    for t in range(max_len):
        visited = set()
        checked = set()

        for robot in range(x):
            if t < len(moving[robot]):
                pos = moving[robot][t]

                if pos not in visited and pos not in checked:
                    visited.add(pos)

                elif pos in visited and pos not in checked:
                    answer += 1
                    checked.add(pos)
                    
    return answer
