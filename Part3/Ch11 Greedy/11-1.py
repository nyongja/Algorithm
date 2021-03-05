# 모험가 길드

if __name__ == "__main__" :
    n = int(input())
    fear = list(map(int, input().split()))
    fear.sort()
    group = list()
    result = 0
    for i in fear :
        if i == len(group)+1 :
            result += 1
            group.clear()
        else :
            group.append(i)
    
    print(result)