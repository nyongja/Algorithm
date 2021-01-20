# 15-2 28. 고정점 찾기

def binary_search(num, start, end) :
    mid = (start + end) // 2
    if start > end :
        return -1
    if num[mid] == mid :
        return mid
    elif num[mid] > mid :
        return binary_search(num, start, mid-1)
    else :
        return binary_search(num, mid+1, end)


n = int(input())
num = list(map(int, input().split()))

print(binary_search(num, 0, len(num)-1))

