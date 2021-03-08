# 18-4 44. 행성 터널

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 행성의 개수
n = int(input())
parent = [0] * n
edges = []
result = 0
for i in range(n) :
    parent[i] = i

x = []
y = []
z = []

for i in range(n) :
    # 행성의 x, y, z 좌표
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))
x.sort()
y.sort()
z.sort()

for i in range(n-1) :
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
edges.sort() # cost 기준으로 정렬

for edge in edges : # 최소 edge 부터 시작해서 사이클이 아닌경우 union
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b) 
        result += cost
print(result)