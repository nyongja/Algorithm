# 12-1 럭키 스트레이트

if __name__ == "__main__" :
    n = input()

    left = 0
    right = 0
    center = int(len(n) / 2)
    for i in range(center) :
        left += int(n[i])
        right += int(n[center + i])
    if left == right :
        print("LUCKY")
    else : print("READY")