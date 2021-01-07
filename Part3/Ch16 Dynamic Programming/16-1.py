# 16-1 31. 금광

def find_max_gold(n, m) :
    mine = list(map(int, input().split()))
    index = 0
    dp_mine = []
    for _ in range(n) :
        dp_mine.append(mine[index:index + m]) # slicing 개념
        index += m

    for j in range(1, m) :
        for k in range(n) :
            # 왼쪽 위에서 오는 경우
            if k == 0 :
                left_up = 0
            else :
                left_up = dp_mine[k-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if k == n-1 :
                left_down = 0
            else :
                left_down = dp_mine[k+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp_mine[k][j-1]
            dp_mine[k][j] = dp_mine[k][j] + max(left_up, left_down, left)

    result = 0
    for l in range(n) :
        result = max(result, dp_mine[l][-1])
    print(result)

if __name__ == "__main__" : 
    t = int(input())
    for _ in range(t) :
        n, m = map(int, input().split())
        find_max_gold(n, m)

    