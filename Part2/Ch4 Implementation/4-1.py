def check_position(x, y, n) :
    if x < 1 or x > n or y < 1 or y > n:
        return False
    return True
 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = {'L' : 0, 'R' : 1, 'U' : 2, 'D' : 3}

def solution(n, plan, x, y) :    
    for p in plan :
        if check_position(x+dx[move[p]], y+dy[move[p]], n) :
            x += dx[move[p]]
            y += dy[move[p]]
    return x, y     


if __name__ == "__main__" : 
    n = int(input())
    plan = list(input().split())
    x, y = solution(n, plan, 1, 1)
    print(x, y)