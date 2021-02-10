# 12-3 09. 문자열 압축

def solution(s):
    answer = 0
    answer = len(s)
    for length in range(1, len(s)) :
        tmp = [s[i:i+length] for i in range(0, len(s), length)]
        prev = tmp[0]
        tmp_answer = ""
        cnt = 1
        for i in range(1, len(tmp)) :
            if prev == tmp[i] :
                cnt += 1
            else :
                if cnt == 1 :
                    tmp_answer += prev
                else :
                    tmp_answer += str(cnt) + prev
                    cnt = 1
            prev = tmp[i]
        if cnt == 1 :
            tmp_answer += prev
        else :
            tmp_answer += str(cnt) + prev
        
        if answer > len(tmp_answer) :
            answer = len(tmp_answer)
    print(answer)

s = input()
solution(s)
