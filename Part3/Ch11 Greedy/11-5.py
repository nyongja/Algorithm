# 11-5 5. 볼링공 고르기

n, m = map(int, input().split())
array = list(map(int, input().split()))
count = [0 for _ in range(m)]

for i in array :
    count[i-1] += 1

result = 0

for i in range(0, m) :
    n -= count[i-1]
    result += count[i-1] * n

print(result) 