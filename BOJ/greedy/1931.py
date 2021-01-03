import sys

N = int(input())

meetings = []
for _ in range(N) :
  meetings.append(list(map(int, sys.stdin.readline().split())))
#끝나는 시간을 기준으로 정렬
meetings.sort(key=lambda x : (x[1],x[0]))

max_cnt = 1
end_time = meetings[0][1]
for i in range(1, len(meetings)) :
  if end_time <= meetings[i][0] :
    end_time = meetings[i][1]
    max_cnt += 1

print(max_cnt)