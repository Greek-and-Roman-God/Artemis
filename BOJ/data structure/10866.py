import sys

def push_front(X, queue) :
  queue.insert(0, X)

def push_back(X, queue) :
  queue.append(X)

def size(queue) :
  return len(queue)

def pop_front(queue) :
  if not size(queue) :
    print(-1)
  else :
    print(queue[0])
    del queue[0]

def pop_back(queue) :
  if not size(queue) :
    print(-1)
  else :
    print(queue[-1])
    del queue[-1]

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
for _ in range(N) :
  command = list(sys.stdin.readline().split())
  if command[0] == "push_front" :
    push_front(command[1], queue)
  elif command[0] == "push_back" :
    push_back(command[1], queue)
  elif command[0] == "pop_front" :
    pop_front(queue)
  elif command[0] == "pop_back" :
    pop_back(queue)
  elif command[0] == "size" :
    print(size(queue))
  elif command[0] == "empty" :
    empty(queue)
  elif command[0] == "front" :
    front(queue)
  elif command[0] == "back" :
    back(queue)