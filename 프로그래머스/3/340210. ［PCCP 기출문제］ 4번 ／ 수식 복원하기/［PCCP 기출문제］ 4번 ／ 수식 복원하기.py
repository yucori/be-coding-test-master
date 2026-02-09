def n_to_ten(n, base):
    temp = 0
    idx = 0
    for digit in reversed(n):
        temp += int(digit) * (base ** idx)
        idx+=1
    return temp

def ten_to_n (n, base):
    if n == 0:
        return "0"
    temp = ""
    while n > 0:
        temp = str(n % base) + temp
        n //= base
    return temp

def solution(expressions):
    answer = []
    
    # 진법 후보의 최댓값 구하기
    max_base = 0
    for exp in expressions:
        for char in exp:
            if '0' <= char <= '9':
                max_base = max(max_base, int(char))
    
    min_base = max_base + 1
    
    # 정답 진법이 될 수 있는 후보군 산정
    possible_bases = []
    for base in range(min_base, 10):
        is_match = True
        for exp in expressions:
            a, op, b, _, c = exp.split()
            
            if c == 'X': 
                continue
            
            # 10진수로 변환하여 계산
            val_a = n_to_ten(a, base)
            val_b = n_to_ten(b, base)
            val_c = n_to_ten(c, base)
            
            if op == '+':
                if val_a + val_b != val_c:
                    is_match = False
                    break
            else:
                if val_a - val_b != val_c:
                    is_match = False
                    break
        
        if is_match:
            possible_bases.append(base)

    # 수식 복원하기
    for exp in expressions:
        a, op, b, _, c = exp.split()
        
        if c != 'X': 
            continue
        
        # 가능한 모든 진법으로 계산해보기
        results = set()
        for base in possible_bases:
            val_a = n_to_ten(a, base)
            val_b = n_to_ten(b, base)
            
            if op == '+':
                res_10 = (val_a + val_b) 
            else:
                res_10 = (val_a - val_b)

            # 다시 n진법으로 변환하여 set에 저장
            results.add(ten_to_n(res_10, base))
        
        # 정정한 수식 저장
        if len(results) == 1:
            res_real = list(results)[0]
            answer.append(f"{a} {op} {b} = {res_real}")
        else:
            answer.append(f"{a} {op} {b} = ?")
            
    return answer