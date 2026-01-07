n, k = map(int, input().split())
coins = []

for _ in range(n):
  coins.append(int(input()))

v = [0] * (k + 1)
v[0] = 1

for coin in coins:
  for i in range(coin, k + 1):
    v[i] += v[i - coin]

print(v[k])