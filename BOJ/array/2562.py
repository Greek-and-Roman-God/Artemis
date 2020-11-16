list = [None] * 9

for i in range(0,9) :
  list[i] = int(input())

print(max(list))
print(list.index(max(list))+1)