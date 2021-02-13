# 15-1 27. 정렬된 배열에서 특정 수의 개수 구하기

def first(num, target, start, end) : # 첫 번재 등장한 원소 찾는 함수
    while start <= end :
        mid = (start + end) // 2
        if num[mid] == target :
            if (num[mid-1] == target) and mid != 0 :
                end = mid - 1
            elif mid == 0 :
                return 0
            else :
                return mid
        elif num[mid] > target :
            end = mid - 1
        elif num[mid] < target :
            start = mid + 1
    return None

def last(num, target, start, end) :
    while start <= end :
        mid = (start + end) // 2

        if num[mid] == target :
            if (num[mid+1] == target) and mid != len(num)-1 :
                start = mid + 1
            elif mid == len(num) - 1 :
                return len(num) - 1
            else :
                return mid
        elif num[mid] > target :
            end = mid - 1
        elif num[mid] < target :
            start = mid + 1
    return None

if __name__ == "__main__" :
    n, x = map(int, input().split())
    
    num = list(map(int, input().split()))
    
    f_index = first(num, x, 0, n-1)
    l_index = last(num, x, 0, n-1)
    if f_index == None or l_index == None :
        answer = -1
    else :
        answer = l_index - f_index + 1

    print(answer)