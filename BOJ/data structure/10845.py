import sys

def push(X, queue) :
  queue.append(X)

def size(queue) :
  return len(queue)

def pop(queue) :
  if not size(queue) :
    print(-1)
  else :
    print(queue[0])
    del queue[0]

def empty(queue) :
  if not size(queue) :
    print(1)
  else :
    print(0)

def front(queue) :
  if not size(queue) :
    print(-1)
  else :
    print(queue[0])

def back(queue) :
  if not size(queue) :
    print(-1)
  else :
    print(queue[-1])

N = int(input())
queue = []
for command in range(N) :
  command = list(sys.stdin.readline().split())
  if command[0] == 'push' :
    push(command[1], queue)
  elif command[0] == 'pop' :
    pop(queue)
  elif command[0] == 'size' :
    print(size(queue))
  elif command[0] == 'empty' :
    empty(queue)
  elif command[0] == 'front' :
    front(queue)
  elif command[0] == 'back' :
    back(queue)