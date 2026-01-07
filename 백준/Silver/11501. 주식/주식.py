t = int(input())
tcs = []
ans_list = []
for _ in range(t):
  n = int(input())
  tcs.append(list(map(int, input().split())))

for tc in tcs:
  sell = tc[-1]
  ans = 0
  for i in range(len(tc)-2, -1, -1):
    if tc[i]>sell:
      sell = tc[i]
    ans += sell-tc[i]
  ans_list.append(ans)

for j in ans_list:
  print(j)
  