import heapq

INF = int(1e9)

V, E = map(int, input().split())
board = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    board[a].append((b, c))
    board[b].append((a, c))

M, X = map(int, input().split())
macs = list(map(int, input().split()))

S, Y = map(int, input().split())
stars = list(map(int, input().split()))

def di(starts):
    dist = [INF] * (V + 1)
    hq = []

    for s in starts:
        dist[s] = 0
        heapq.heappush(hq, (0, s))

    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue

        for nxt, c in board[node]:
            new_cost = cost + c
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))

    return dist


dm = di(macs)
ds = di(stars)

ans = INF

for i in range(1, V + 1):
    if i in macs or i in stars:
        continue

    if dm[i] <= X and ds[i] <= Y:
        ans = min(ans, dm[i] + ds[i])

if ans == INF:
    print(-1)
else:
    print(ans)