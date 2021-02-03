import sys

def push(X, stack) :
  stack.append(X)
  return

def size(stack) :
  return len(stack)

def pop(stack) :
  if size(stack) == 0 :
    print(-1)
  else :
    print(stack[-1])
    #remove를 쓰면 해당 숫자를 스택에서 전부 지워버리게 되므로
    #del을 써서 마지막 숫자만 지워야 한다
    del stack[-1]

def empty(stack) :
  if size(stack) == 0 :
    print(1)
  else :
    print(0)
  return

def top(stack) :
  if size(stack) == 0 :
    print(-1)
  else :
    print(stack[-1])
  return

N = int(input())

stack = []
for _ in range(N) :
  command = list(sys.stdin.readline().strip().split())
  if command[0] == "push" :
    push(command[1], stack)
  elif command[0] == "size" :
    print(size(stack))
  elif command[0] == "pop" :
    pop(stack)
  elif command[0] == "empty" :
    empty(stack)
  else :
    top(stack)