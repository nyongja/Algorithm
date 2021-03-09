# 18-5 45. 최종순위

from collections import deque
 
def topology_sort(indegree, graph, n) :
    result = []
    q = deque()

    for i in range(1, n+1) :
       if indegree[i] == 0 :
           q.append(i)

    for i in range(n) :
        if len(q) == 0 :
            return "IMPOSSIBLE"
        if len(q) > 1 :
            return "?"
        now = q.popleft()
        result.append(now)
        for i in range(1, n+1) :
            if graph[now][i] :
                indegree[i] -= 1
                if indegree[i] == 0 :
                    q.append(i)


    result_s = ""
    for i in result :
        result_s += str(i) + " "
    return result_s[:-1]

t = int(input()) # 테스트 케이스 수
while t > 0 :
    t -= 1
    n = int(input()) # 팀의 수
    rank = list(map(int, input().split())) # 작년 순위
    indegree = [0] * (n+1) # 진입차수 정보
    graph = [[False] * (n+1) for i in range(n+1)] # 그래프 정보
    for i in range(n) :
        for j in range(i+1, n) :
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1
    m = int(input()) # 상대적인 등수가 바뀐 쌍의 수
    for _ in range(m) :
        a, b = map(int, input().split())
        if graph[a][b] :
            graph[b][a] = True
            graph[a][b] = False
            indegree[a] += 1
            indegree[b] -= 1
        else :
            graph[a][b] = True
            graph[b][a] = True
            indegree[b] += 1
            indegree[a] -= 1

    print(topology_sort(indegree, graph, n))
    