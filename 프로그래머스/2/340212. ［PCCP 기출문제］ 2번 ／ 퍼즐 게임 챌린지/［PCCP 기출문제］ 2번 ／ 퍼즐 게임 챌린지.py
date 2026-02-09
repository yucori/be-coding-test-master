def solution(diffs, times, limit):
    def check(level):
        temp = times[0]
        for i in range(1, len(diffs)):
            if diffs[i] > level:
                cal = diffs[i] - level
                temp += (cal+1) * times[i]
                temp += cal * times[i-1]
            else:
                temp += times[i]
            if temp > limit:
                return False
        return True
    
    l, r = 1, max(diffs)

    while l < r:
        mid = (l + r) // 2
        if check(mid):
            r = mid
        else:
            l = mid + 1

    return l