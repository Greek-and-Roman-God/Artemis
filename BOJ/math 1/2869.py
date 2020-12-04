A, B, V = map(int,(input().split()))

move = A - B
day = ((V-A) // move) #미끄러지기 전에 도착하는 경우를 고려
#하루가 지나면 무조건 도착하므로 +1
#첫 날에 움직인 횟수가 세지지 않는 경우가 있으므로 if else
#ex)5 1 6
day += 1 if (V-A) % move == 0 else 2
print(day)