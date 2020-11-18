#제일 작은 걸 1개 자를 때의 길이를 최대값으로 잡아서 이진탐색

#메모리초과로 실패

from sys import stdin
import copy

k, n = map(int, stdin.readline().split())
K = []
for _ in range(k) :
  K.append(int(stdin.readline()))
N = n   #재귀호출시 n값을 고정시키기 위해 사용하는 변수

def cutting_lan(N, n, K) :
  temp = copy.deepcopy(K)   #K값을 고정시키기 위해 깊은 복사
  cnt = 0
  lan = temp[0] // n
  for i in range(k) :
    cnt += temp[i] // lan
    temp[i] %= lan
  if cnt > N :
    cutting_lan(N, n-1, K)
  else :
    print(lan)
    return

cutting_lan(N, n, K)