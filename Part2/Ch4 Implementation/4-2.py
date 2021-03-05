def solution(n):
    result = 0
    # 1분에 '3'이 등장하는 초
    sec_count = 0
    for sec in range(0, 60) :
        if sec % 10 == 3 or sec // 10 == 3 :
            sec_count += 1
    # 1시간에 '3'이 등장하는 분 
    min_count = 0
    for min in range(0, 60) :
        if min % 10 == 3 or min // 10 == 3 :
            min_count += 60
        else :
            min_count += sec_count
    # '3'이 등장하는 시간에 따른 결과 계산
    for hour in range(0, n+1) :
        if hour % 10 == 3 or hour // 10 == 3 :
            result += 3600
        else :
            result += min_count

    return result        




if __name__ == "__main__" :
    n = int(input())
    print(solution(n))