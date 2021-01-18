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

if __name__ == '__main__':
    n, m = map(int, input().split()) # n = 여행지 수, m = 여행 계획에 속한 도시 수
    
    parent = [0] * (n + 1)

    # 부모를 자기 자신으로 초기화
    for i in range(n) :
        parent[i] = i

    # union 연산 각각 수행
    for i in range(n) :
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)) :
            if tmp[j] == 1 :
                union_parent(parent, i, j)

    plan = list(map(int, input().split()))

    result = True
    for i in range(m-1) :
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]) :
            result = False

    if result :
        print("YES")
    else :
        print("NO")