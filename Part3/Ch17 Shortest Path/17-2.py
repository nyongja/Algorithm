# 17-2 38. 정확한 순위

INF = int(1e9)
n, m = map(int, input().split()) # n = 학생수, m = 성ㅇ적을 비교한 횟수
graph = [[INF]*n for _ in range(n)]

# 자기 자신으로 가는 부분 초기화
for i in range(n) :
    for j in range(n) :
        if i == j :
            graph[i][j] = 0

# 비교가 가능한지 체크
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(n) :
    count = 0
    for j in range(n) :
        if graph[i][j] != INF or graph[j][i] != INF :
            count += 1
    if count == n :
        result += 1

print(result)