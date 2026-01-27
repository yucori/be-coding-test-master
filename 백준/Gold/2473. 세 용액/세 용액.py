n = int(input())
pos = []
neg = []
board = list(map(int, input().split()))
board.sort()

ans = 9999999999
ans_list = ()

for i in range(n-2):
  left = i+1
  right = n-1
  while left<right:
    temp = board[i]+board[left]+board[right]
    abs_tmp = abs(temp)
    
    if abs_tmp<ans:
      ans = abs_tmp
      ans_list = (board[i], board[left], board[right])
    if temp==0:
      print(*ans_list)
      exit()
    if temp<0:
      left += 1
    if temp>0:
      right -= 1
  
print(*ans_list)