import sys

N = int(input())
N_cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
M_cards = list(map(int, sys.stdin.readline().split()))

N_cards.sort()

for card in M_cards :
  left = 0
  right = N
  while left < right :
    mid = (left + right) // 2
    if card == N_cards[mid] :
      print(1, end=' ')
      break
    elif card > N_cards[mid] :
      left = mid + 1
    else :
      right = mid
  else :
    print(0, end=' ')