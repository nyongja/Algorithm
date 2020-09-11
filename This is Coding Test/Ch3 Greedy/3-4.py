def solution1(n, k) :
    count = 0
    
    # n이 k로 나눌 수 있을 때까지 -1
    while n%k != 0 and n!= 1:
        n -= 1
        count += 1
    
    # n을 k로 나누기
    while n%k == 0 and n!= 1 :
        n /= k
        count +=1
    
    if n!= 1 :
        count += round(n-1)
    return count

def solution2(n, k) :
    count = 0 
    while True : 
        # ( N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
        # N을 K로 나눴을 때 나머지 구하는 과정
        target = (n // k) * k
        count += (n - target)
        n = target
        
        # 더 이상 나눌 수 없는 경우
        if n < k :
            break
        
        # N을 K로 나누기
        count +=1
        n //= k
        
    count += (n-1)
    return count

if __name__ == "__main__" :
    n, k = map(int, input().split())
    print(solution1(n, k))
    print(solution2(n, k))