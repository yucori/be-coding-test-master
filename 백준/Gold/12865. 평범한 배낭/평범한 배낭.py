n, k = map(int, input().split())

max_list = [0] * (k+1)

for _ in range(n):
  w, v = map(int, input().split())
  
  for i in range(k, w-1, -1):
    max_list[i] = max(max_list[i], max_list[i-w]+v)

print(max_list[k])
