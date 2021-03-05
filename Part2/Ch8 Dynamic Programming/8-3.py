# 8-3 바닥공사

def solution(n) :
    d = [0] * 1001 

    d[1] = 1
    d[2] = 3
    if n == 1 or n == 2 : return d[n]

    for i in range(3, n + 1) :
        d[i] += d[i-1] * 1
        d[i] += d[i-2] * 2
        d[i] = d[i] % 796796

    return d[n]



if __name__ == "__main__" :
    n = int(input())
    print(solution(n))