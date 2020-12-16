# 개미 전사
def solution(food_storage):
    answer = 0
    d = [0] * 100 
    
    for index, value in enumerate(food_storage):
        if index == 0 or index == 1 :
            d[index] = value
        else :
            d[index] = max(d[0:index-1]) + value
    
    answer = max(d)
    return answer

if __name__ == "__main__" :
    n = int(input())
    food_storage = list(map(int, input().split()))
    print(solution(food_storage))