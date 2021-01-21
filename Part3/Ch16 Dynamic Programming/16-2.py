# 16-2 32. 정수삼각형

n = int(input())

triangle = []

for _ in range(n) :
    triangle.append(list(map(int, input().split())))

for line in range(n-1, 0, -1) :
    for index in range(len(triangle[line])-1):
        num = max(triangle[line][index], triangle[line][index+1])
        triangle[line-1][index] += num
print(triangle[0][0])