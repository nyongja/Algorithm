# 8-4 효율적인 화폐 구성 
                
def solution(money_list, n, m) :
    d = [10001] * (m + 1)
    d[0] = 0
    for i in range(n) :
        for j in range(money_list[i], m + 1) :
            if d[j - money_list[i]] != 10001 :
                d[j] = min(d[j], d[j - money_list[i]] + 1)
    if d[m] == 100001 :
        return -1
    else :
        return d[m]                          
        
    

if __name__ == "__main__":            
    n, m = map(int, input().split())
    money_list = []
    for _ in range(n) :
        money_list.append(int(input()))
    
    print(solution(money_list, n, m))                                                  