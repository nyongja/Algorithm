# 17-1 37. 플로이드

MAX_NUM = int(1e9)

if __name__ == '__main__':
    n = int(input()) # 도시 개수
    m = int(input()) # 버스 개수
    
    bus_info = [[MAX_NUM for _ in range(n)] for _ in range(n)]

    # 자기 자신으로 가는 곳 0으로 초기화
    for i in range(0, n) :
        for j in range(0, n) :
            if i == j :
                bus_info[i][j] = 0
    # 간선 정보 받기 
    for _ in range(m) :
        departure, arrival, cost = map(int, input().split())
        if bus_info[departure-1][arrival-1] > cost :
            bus_info[departure-1][arrival-1] = cost


    for i in range(0, n) : # i번째 도시를 거쳐서 가는 법 계산하기
        for j in range(0, n) : # j에서
            for k in range(0, n) : # k까지 갈때
                bus_info[j][k] = min(bus_info[j][k], bus_info[j][i] + bus_info[i][k])


    for i in range(0, n) :
        result = ""
        for j in range(0, n) :
            if bus_info[i][j] == MAX_NUM :
                result += "0 "
            else :
                result += str(bus_info[i][j])
                result += " "
        print(result)