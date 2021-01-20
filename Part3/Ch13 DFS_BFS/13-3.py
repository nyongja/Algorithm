# 13-3 17. 경쟁적 전염

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(data, visited, s) :
    queue = deque([])
    
    for i in range(n) :
        for j in range(n) :
            if data[i][j] != 0 :
                queue.append((i, j))
                visited[i][j] = 0
    while queue :
        v = queue.popleft()
        cnt = visited[v[0]][v[1]]
        if cnt == s : return
        for i in range(4) : # 상하좌우
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n : # 실험관 내부인지 확인
                if visited[nx][ny] == cnt+1 : # 이미 방문한 곳인데 같은 초에 일어난 일인지 check
                    if data[nx][ny] > data[v[0]][v[1]] : # 우선순위 바이러스면
                        data[nx][ny] = data[v[0]][v[1]]
                elif visited[nx][ny] == -1 : # 아직 방문 전이라면
                    data[nx][ny] = data[v[0]][v[1]] # 값 바꾸기
                    visited[nx][ny] = cnt + 1
                    queue.append((nx, ny))
    

n, k = map(int, input().split()) # n : 시험관 크기, k : 바이러스 종류 개수
data = []
visited = [[-1]*n for _ in range(n)]
for _ in range(n) :
    data.append(list(map(int, input().split())))

s, x, y = map(int, input().split()) # s : 초, x,y : 바이러스 위치

bfs(data, visited, s)
print(data[x-1][y-1])