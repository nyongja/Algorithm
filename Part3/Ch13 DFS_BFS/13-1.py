# 13-1 15.특정거리의 도시 찾기

# BFS 풀이 방식
from collections import deque
import sys
def bfs(visited, graph, k, start) :
    queue = deque([(start, 0)])
    visited[start] = True
    

    # 몇 번째 방문인지
    answer = []
    while queue :
        v, count = queue.popleft()
        if count == k :
            answer.append(v+1)
        elif count < k :
            for i in graph[v] :
                if visited[i] == False :
                    queue.append((i, count+1))
                    visited[i] = True

    if len(answer) == 0 :
        answer.append(-1)
    answer.sort() 
    return answer

if __name__ == "__main__" :
    # n = 도시 수, m = 도로 수, k = 최단 거리, x = 출발 도시
    input = sys.stdin.readline
 
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    
    for i in range(m) :
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    answer = bfs(visited, graph, k, x-1)
    
    for i in answer :
        print(i)