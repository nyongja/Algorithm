# 18-3 43. 어두운 길

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

if __name__ == "__main__" :
    n, m = map(int, input().split()) # n = 집 수, m = 도로 수

    parent = [0] * n
    
    for i in range(n) :
        parent[i] = i
    
    edges = []
    for i in range(m) :
        x, y, cost = map(int, input().split())
        edges.append((cost, x, y))

    edges.sort()

    result = 0
    for e in edges :
        cost, x, y = e
        if find_parent(parent, x) != find_parent(parent, y) :
            union_parent(parent, x, y)
        else : # 사이클 생김, 연결안해도 됨!
            result += cost
    print(result)
    
