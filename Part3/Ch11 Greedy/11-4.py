# 11-4 4. 만들 수 없는 금액


if __name__ == "__main__" :
    n = int(input()) # 동전 개수
    coin_lst = list(map(int, input().split()))
    coin_lst.sort()

    target = 1
    
    for coin in coin_lst :
        if target < coin : # coin이 더 크면 target을 만들 수 없으므로
            break
        print(target)
        target += coin # 다음에 올 동전은 무조건 coin이상이므로 coin을 더해서 비교


    print(target)