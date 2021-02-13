# 곱하기 혹은 더하기

if __name__ == "__main__" :
    s = input()
    
    answer = 0
    for i in s :
        tmp1 = answer + int(i)
        tmp2 = answer * int(i)
        
        answer = max(tmp1, tmp2)
    
    print(answer)