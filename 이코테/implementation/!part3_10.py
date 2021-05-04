def check(i, j, arr, M) :
    for a in range(M) :
        for b in range(M) :
            if arr[i][j] == 1 and key[a][b] == 1 :
                return False
    return True           

def rotate(key) :
    return list(zip(*arr[::-1]))

def solution(key, lock):
    answer = False
    
    N, M = len(lock), len(key)
    size = N + (M - 1) * 2
    arr = [[0] * size for _ in range(size)]
    for i in range(N) :
        for j in range(N) :
            arr[M+i-1][M+j-1] = lock[i][j]
    
    for _ in range(4) :
        for i in range(size-(M-1)) :
            for j in range(size-(M-1)) :
                for a in range(M) :
                    for b in range(M) :
                        arr[i][j] += key[a][b]
                        if(check(i, j, arr, M)) :
                            return True
                        arr[i][j] -= key[a][b]
        
        rotate_key = rotate(key)
    
    return answer