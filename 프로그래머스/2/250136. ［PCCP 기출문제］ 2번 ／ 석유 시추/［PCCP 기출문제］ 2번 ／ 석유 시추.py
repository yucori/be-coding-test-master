def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0]*m for _ in range(n)]
    result = [0]*m

    def dfs(r, c):
        stack = [(r, c)]
        count = 0
        cols = set()

        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = 1

            count += 1
            cols.add(y)

            for dx, dy in [(0,1),(0,-1),(1,0),( -1,0)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if land[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx,ny))
        return count, cols

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                count, cols = dfs(i, j)
                for col in cols:
                    result[col] += count

    return max(result)