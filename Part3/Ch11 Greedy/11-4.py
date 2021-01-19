# 11-4 4. 만들 수 없는 금액


if __name__ == "__main__" :
    n = int(input()) # 동전 개수
    coin_lst = list(map(int, input().split()))
    coin_lst.sort()

    target = 1
    
    for coin in coin_lst :
        if target < coin :
            break
        print(target)
        target += coin

    print(target)