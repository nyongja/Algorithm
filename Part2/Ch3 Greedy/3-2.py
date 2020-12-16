def the_largest_number_1(n, m, k, num_list) :
    num_list.sort(reverse=True) 
    num = 0
    cnt = 0
    while m > 0 :
        if cnt != k :
            num += num_list[0]
            cnt+=1
        else :
            num += num_list[1]
            cnt = 0
        m-=1
    return num

def the_largest_number_2(n, m, k, num_list) :
    num_list.sort(reverse=True)
    if k >= m :
        num = num_list[0] * m
    else :
        num = num_list[0] * k * (m//k) + num_list[1] * (m - (k * (m//k)))
    return num

if __name__ == "__main__" :
    n, m, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(the_largest_number_1(n, m, k, num_list))
    print(the_largest_number_2(n, m, k, num_list))
