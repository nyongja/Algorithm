# 14-1 23. 국영수
import sys

if __name__ == "__main__" :
    n = int(input())
    score = []

    for i in range(n) :
        score.append(input().split())
    
    score.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for i in score :
        print(i[0])