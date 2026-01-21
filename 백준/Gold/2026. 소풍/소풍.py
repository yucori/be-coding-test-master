import sys
input = sys.stdin.readline

k, n, f = map(int, input().split())

students = [[False] * (n + 1) for _ in range(n + 1)]
s_cnt = [0] * (n + 1)

for _ in range(f):
    a, b = map(int, input().split())
    students[a][b] = True
    students[b][a] = True
    s_cnt[a] += 1
    s_cnt[b] += 1

candidates = []
for i in range(1, n + 1):
    if s_cnt[i] >= k - 1:
        candidates.append(i)

def find_picnic_members(idx, members):
    if len(members) == k:
        for member in members:
            print(member)
        exit()

    for i in range(idx, len(candidates)):
        new_student = candidates[i]
        
        if len(members) + (len(candidates) - i) < k:
            return

        is_friend = True
        for member in members:
            if not students[new_student][member]:
                is_friend = False
                break

        if is_friend:
            members.append(new_student)
            find_picnic_members(i + 1, members)
            members.pop()

find_picnic_members(0, [])
print(-1)
