N = int(input())

result = [1] #슬라이싱을 위해 초기값을 넣음, 시작값은 항상 1
def good_arr(depth, result) :
  for i in range(1, N//2+1) : #N//2자리수까지만 비교하면 된다
    if result[-i:] == result[-(i+i):-i] : #인접한 수가 같으면
      return

  #길이를 처음으로 충족하는 수는 가장 최소값이므로 exit으로 종료
  #여기서 종료를 하지 않으면 시간초과가 난다
  if depth == N :
    print("".join(map(str, result)))
    exit()

  for i in range(3) : #1,2,3을 오름차순으로 붙여준다
    result.append(i+1)
    good_arr(depth+1, result)
    result.pop()

good_arr(1, result)