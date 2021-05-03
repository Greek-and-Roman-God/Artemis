def solution(s):
    answer = int(1e9)
    
    for i in range(1, len(s)//2+2) : #len(s)//2 + 2로 한 이유는 문자열 길이가 1인 경우를 위해
        result = ""
        cnt = 1
        tmp = s[:i] #비교할 문자열을 저장
        for j in range(i, len(s)+i, i) :
            if tmp == s[j:j+i] : #정해진 길이만큼 비교하고 같으면 cnt 올림
                cnt += 1
            else : #다르면 압축 중단
                if cnt == 1 : #압축이 하나도 안 된 경우 문자만 붙임
                    result += tmp
                else : #압축이 됐으면 압축한 숫자와 문자를 붙임
                    result += str(cnt) + tmp
                cnt = 1
                tmp = s[j:j+i] #비교할 문자열 재설정
        answer = min(answer, len(result)) #제일 압축이 많이 된 것을 출력
    
    return answer