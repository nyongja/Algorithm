# 12-2 08. 문자열 재정렬

if __name__ == '__main__': 
    s = input()

    num = 0
    alpha = []
    for i in s :
        if i.isdigit(): 
            num += int(i)
        else :
            alpha.append(i)
    alpha.sort()
    alpha.append(str(num))

    print(''.join(alpha))