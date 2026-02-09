2
3
4
5
6
7
8
9
10
11
def solution(diffs, times, limit):
    answer, left, right = 1, 1, 100_000
    while left <= right:
        level = (left + right) // 2
        if sum(times[i] if diffs[i] <= level else (diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
               for i, _ in enumerate(diffs)) > limit:
            left = level + 1
        else:
            answer, right = level, level - 1
    return answer
