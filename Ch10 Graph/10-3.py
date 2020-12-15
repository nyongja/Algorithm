# 커리큘럼
from collections import deque
import copy

def topology_sort(n, indegree, time, graph) :
    q = deque()
    result = copy.deepcopy(time)
    for i in range(1, n + 1) :  
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()
        for i in graph[now] :
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, n + 1) :
        print(result[i])

if __name__ == "__main__" :
    n = int(input()) 
    indegree = [0] * (n+1)
    graph = [[] for i in range(n + 1)]
    time = [0] * (n + 1)

    for i in range(1, n+1) :
        data = list(map(int, input().split()))
        time[i] = data[0]
        for x in data[1 : -1] :
            indegree[i] += 1
            graph[x].append(i)
    topology_sort(n, indegree, time, graph)