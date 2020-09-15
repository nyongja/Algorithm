def change(money):
    coin_types = [500, 100, 50, 10]
    count = 0
    for coin in coin_types :
        count += money // coin
        money %= coin
    return count

if __name__ == "__main__" :
    money = int(input())
    count = change(money)
    print(count)