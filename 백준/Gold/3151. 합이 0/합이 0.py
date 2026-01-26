n = int(input())
board = list(map(int, input().split()))
board.sort()
cnt = 0

for i in range(n-2):
    left = i+1
    right = n-1
    while left<right:
        temp = board[i]+board[left]+board[right]
        if temp==0:
            if board[left]==board[right]:
                m = right-left+1
                cnt += (m*(m-1))//2
                break
            else:
                l_cnt = 1
                r_cnt = 1
                while left+1<right and board[left]==board[left+1]:
                    l_cnt += 1
                    left += 1
                while right-1>left and board[right]==board[right-1]:
                    r_cnt += 1
                    right -= 1
                cnt += l_cnt*r_cnt
                left += 1
                right -= 1
        elif temp<0:
            left += 1
        else:
            right -= 1

print(cnt)