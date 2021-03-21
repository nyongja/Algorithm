# 12-5 11. 뱀

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

board = [[0] * n for _ in range(n)]
snake = [[0] * n for _ in range(n)]
snake[0][0] = 1
for _ in range(k) : # 보드에 사과 위치 저장
    i, j = map(int, input().split())
    board[i-1][j-1] = 1
print(board)
l = int(input()) # 뱀의 방향 변환 횟수
move = []
for _ in range(l) :
    x, c = input().split()
    move.append((int(x), c))


x_pos = [0, 1, 0, -1]
y_pos = [1, 0, -1, 0]


def game() :
    time = 0 
    pos = 0 # 오, 위, 왼, 아
    head_pos_x = 0
    head_pos_y = 0
    tail_pos_x = 0
    tail_pos_y = 0
    for x, c in move :
        for i in range(x) :
            time += 1
            head_pos_x += x_pos[pos]
            head_pos_y += y_pos[pos]
            if head_pos_x >= n or head_pos_y >= n or head_pos_x < 0 or head_pos_y < 0 : # 벽에 부딪히면
                print("case 1")
                return time
            if snake[head_pos_x][head_pos_y] == 1 : # 자기 자신 몸 만나면
                print("case 2")
                return time
            if board[head_pos_x][head_pos_y] == 0 : # 사과가 없으면
                snake[tail_pos_x][tail_pos_y] = 0
                tail_pos_x += x_pos[pos]
                tail_pos_y += y_pos[pos]
            snake[head_pos_x][head_pos_y] = 1
            for i in snake :
                print(i)
            print(" ")
            
        if c == "L" :
            pos = (pos - 1) % 4
        else :
            pos = (pos + 1) % 4
        
    return time

print(game())