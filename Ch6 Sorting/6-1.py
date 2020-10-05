def sort(num_list) :
    num_list.sort(reverse = True)
    return

if __name__ == "__main__" :
    n = int(input())
    num_list = []
    for i in range(n) :
        num_list.append(int(input()))
   
    sort(num_list)
    
    for i in num_list :
        print(i, end = " ")