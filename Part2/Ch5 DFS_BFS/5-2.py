from collections import deque

def check_position(maze, x, y, n, m) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False
    elif maze[x][y] != 1 : # 괴물이 있거나 이미 지나친 곳
        return False
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maze, n, m):
    queue = deque()
    queue.append((0, 0))
    maze[0][0] = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            if check_position(maze, x+dx[i], y+dy[i], n, m) :
                queue.append((x+dx[i], y+dy[i]))
                maze[x+dx[i]][y+dy[i]] = maze[x][y] + 1
    return maze[n-1][m-1]

if __name__ == "__main__" :
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        maze.append(list(map(int, input())))

    print(bfs(maze, n, m))
    print(maze)