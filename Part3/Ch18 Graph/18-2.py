# 18-2 42. 탑승구

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
    g = int(input()) # 탑승구의 수
    p = int(input()) # 비행기의 수
    parent = [0] * (g + 1)

    # 자기자신으로 부모 초기화
    for i in range(1, g+1) :
        parent[i] = i
    
    result = 0
    for _ in range(p) :
        g_i = int(input())
        tmp_parent = find_parent(parent, g_i)
        if tmp_parent == 0 :
            break
        else :
            result += 1
            union_parent(parent, tmp_parent, tmp_parent - 1)
    print(result)