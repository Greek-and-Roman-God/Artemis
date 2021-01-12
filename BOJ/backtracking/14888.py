N = int(input())
nums = list(map(int, input().split()))

operator_num = list(map(int, input().split())) #연산자 개수
operators = [] #연산자 개수만큼 리스트에 저장
for i in range(operator_num[0]) :
  operators.append('+')
for i in range(operator_num[1]) :
  operators.append('-')
for i in range(operator_num[2]) :
  operators.append('*')  
for i in range(operator_num[3]) :
  operators.append('//')
visited = [False] * len(operators) #각 연산자 방문 여부

expression = [] #최종표현식
result = [] #나올 수 있는 모든 값들 저장하는 리스트
def backtracking(temp, N, M, value) :
  if temp == M :
    value = nums[0] #식의 초기값은 항상 첫번째 숫자
    for i in range(len(expression)) :
      if expression[i] == '+' :
        value += nums[i+1]
      elif expression[i] == '-' :
        value -= nums[i+1]
      elif expression[i] == '*' :
        value *= nums[i+1]
      elif expression[i] == '//' :
        if value < 0 : #음수일 경우 양수로 바꿔서 계산
          value = -(-value // nums[i+1])
        else :
          value //= nums[i+1]                      
    result.append(value)
    return
  
  for i in range(len(visited)) :
    if not visited[i] :
      visited[i] = True
      expression.append(operators[i])
      backtracking(temp+1, N, M, value)
      expression.pop()
      visited[i] = False

backtracking(0, N, len(operators), 0)
print(max(result))
print(min(result))