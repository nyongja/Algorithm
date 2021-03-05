# 15-3 29. 공유기 설치


# 집 개수, 공유기 개수 input
n, c = list(map(int, input().split(' ')))
house = [int(input()) for _ in range(n)]
house.sort()

#start = house[1] - house[0] # 집의 좌표 중에 가장 작은 값
start = 1
end = house[-1] - house[0] # 집의 좌표 중에 가장 큰 값
result = 0


while(start <= end) :
    mid = (start + end) // 2 # mid는 가장 인접한 두 공유기 사이의 거리(gap)을 의미
    value = house[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기 설치
    for i in range(1, n) : # 앞에서부터 차근차근 설치
        if house[i] >= value + mid :
            value = house[i]
            count += 1
    if count >= c : # C개 이상 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid # 최적의 결과를 저장
    else : # C개 이상 공유기를 설치할 수 없는 경우, 거리를 감소
        end = mid - 1
print(result)
