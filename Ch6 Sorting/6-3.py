def array_swap(a, b, k) :
    a.sort()
    b.sort(reverse = True)

    for i in range(k) :
        if a[i] < b[i] :
            a[i], b[i] = b[i], a[i]
    return

if __name__ == "__main__" :
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    array_swap(a, b, k)
    answer = sum(a)
    print(answer)