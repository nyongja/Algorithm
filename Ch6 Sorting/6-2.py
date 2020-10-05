def setting(data):
    return data[1]

if __name__ == "__main__" :
    n = int(input())
    student = []
    for i in range(n) :
        input_data = input().split()
        student.append((input_data[0], input_data[1]))
    
    # case 1
    student.sort(key = setting)
    # case 2
    # student.sort(key = lambda student : student[1])
    for i in student :
        print(i[0], end = ' ')