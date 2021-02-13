# 도시 분할 계획
 
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_house(parent, a, b) :
    if parent[a] != parent[b] :
        a = find_parent(parent, a) 
        b = find_parent(parent, b)
        if a < b :
            parent[b] = a
        else :
            parent[a] = b
        
if __name__ == "__main__" :
    n, m = map(int, input().split())

    parent = [0] * (n + 1)
    # 부모 테이블 초기화
    for i in range(n) :
        parent[i] = i

    edges = []
    for _ in range(m) :
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
    
    edges.sort()

    result = 0
    last = 0
    for edge in edges :
        cost, a, b = edge
        # 사이클이 발생하지 않은 경우에만(최소 신장이어야 하므로)
        if find_parent(parent, a) != find_parent(parent, b) :
            union_house(parent, a, b)
            result += cost
            last = cost

    print(result - last)