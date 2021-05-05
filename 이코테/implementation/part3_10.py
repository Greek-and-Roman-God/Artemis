def attach(arr, key, i, j, M) :
    for a in range(M) :
        for b in range(M) :
            arr[i+a][j+b] += key[a][b]
    
def detach(arr, key, i, j, M) :
    for a in range(M) :
        for b in range(M) :
            arr[i+a][j+b] -= key[a][b]

def check(arr, N, M) :
    for i in range(N) :
        for j in range(N) :
            if arr[M+i][M+j] != 1 : #키 값이 2이거나 0이라면 맞지 않는 것
                return False
    return True
    
def rotate(key) :
    return list(zip(*key[::-1]))

def solution(key, lock) :
    M, N = len(key), len(lock)
    
    #자물쇠를 중앙에 배치
    arr = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    for i in range(N) :
        for j in range(N) :
            arr[i+M][j+M] = lock[i][j]
    
    for _ in range(4) : #네 방향으로 회전해가며 열쇠가 맞는지 확인
        for i in range(M+N) :
            for j in range(M+N) :
                attach(arr, key, i, j, M) #열쇠 꽂기
                if(check(arr, N, M)) : #열쇠가 맞다면 True 리턴
                    return True
                detach(arr, key, i, j, M) #열쇠 빼기
        key = rotate(key) #키 방향 돌리기
    
    return False