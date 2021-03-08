# 17-3 39. 화성 탐사

import heapq
import sys

INF = int(1e9)


def dijkstra(distance, array) :
    q = []
    heapq.heappush(q, (array[0][0], 0, 0))
    distance[0][0] = array[0][0]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q : 
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist :
            continue
        for d in range(4) :
            nx = dx[d]
            ny = dy[d]
            if (x + nx >= 0)  and (x + nx < n) and (y + ny >= 0) and (y + ny < n) :
                cost = dist + array[x + nx][y + ny]
                if cost < distance[x + nx][y + ny] :
                    distance[x + nx][y + ny] = cost
                    heapq.heappush(q, (cost, x + nx, y + ny))

# 테스트 케이스 수 입력받기
t = int(input())

while t > 0 :
    t -= 1
    n = int(input()) # 탐사 공간 크기
    array = []
    for _ in range(n) :
        array.append(list(map(int, input().split())))
    distance = [[INF] * n for _ in range(n)]
    dijkstra(distance, array)
    print(distance[n-1][n-1])


    
    
