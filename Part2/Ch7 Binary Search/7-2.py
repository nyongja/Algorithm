# 떡볶이 떡 만들기

def solution(m, rice_cake) :
    rice_cake.sort()
    start = 0
    end = rice_cake[-1]
    answer = 0 

    while start <= end :
        cut = (start + end) // 2
        length = 0

        for i in rice_cake :
            if i > cut :
                length += i - cut

        if length == m :
            answer = cut
            return answer
        elif length > m :
            answer = cut
            # 더 짧은 경우있는지 확인
            start = cut + 1
        else :
            end = cut - 1
    return answer
        
if __name__ == "__main__" :
    n, m = map(int, input().split())
    rice_cake = list(map(int, input().split()))
    print(solution(m, rice_cake))