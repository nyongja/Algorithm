def solution(N, stages):
    answer = []
    per_num = len(stages)

    fail_rate = []
    
    for i in range(1, N+1) : 
        not_clear = stages.count(i)

        if per_num == 0 :
            fail = 0
        else :
            fail = not_clear/per_num
        fail_rate.append((i, fail))
        per_num -= not_clear

    answer = sorted(fail_rate, key=lambda fail_rate: fail_rate[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer