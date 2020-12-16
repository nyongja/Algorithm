def binary_search(sell_list, item, start, end) :
    while start <= end :
        mid = (start + end) // 2
        if item == sell_list[mid] :
            return "yes"
        elif item < mid :
            end = mid - 1
        else :
            start = mid + 1
    return "no"

if __name__ == "__main__" :
    n = int(input())
    sell_list = list(map(int, input().split()))
    m = int(input())
    buy_list = list(map(int, input().split()))
    sell_list.sort()
    for i in buy_list :
        print(binary_search(sell_list, i, 0, n-1))