def check_position(x, y) :
    # 체스판 범위 넘어가지 않았는지 check
    if x < 0 or x > 8 or y < 0 or y > 8 :
        return False
    return True

# 나이트가 이동할 수 있는 모든 types
dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

def solution(position):
    result = 0

    x = ord(position[0])-97 # ASCII코드로 변경
    y = int(position[1])-1

    for i in range(len(dx)) :
        if check_position(x+dx[i], y+dy[i]) : result += 1
        
    return result

if __name__ == "__main__" :
    # 현재 나이트의 위치
    position = input()
    print(solution(position))