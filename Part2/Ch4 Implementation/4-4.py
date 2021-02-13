move_type = {0 : (0, -1), 1 : (1, 0), 2 : (0, 1), 3 : (-1, 0)}
back_type = {0 : (0, 1), 1 : (-1, 0), 2 : (0, -1), 3 : (1, 0)}

def check_position(n, m, a, b, game_map):
    if game_map[a][b] == 0 or a < 0  or a > n or b < 0 or b > m:
        return False
    return True

def solution(n, m, a, b, d, game_map) :
    result = 0
 
    while True :
        d = (d+1)%4
        if check_position(n, m, a + move_type[d][0], b + move_type[d][1], game_map) :
            a = a + move_type[d][0]
            b = b + move_type[d][1]
            result += 1
        elif check_position(n, m, a + back_type[d][0], b + back_type[d][1], game_map) :
            a = a + back_type[d][0]
            b = b + back_type[d][1]
            result += 1
        else :
            break
    return result

if __name__ == "__main__" :
    n, m =  map(int, input().split())
    a, b, d = map(int, input().split())
    
    game_map = []
    for i in range(n) :
        game_map.append(list(map(int, input().split())))

    print(solution(n, m, a, b, d, game_map))