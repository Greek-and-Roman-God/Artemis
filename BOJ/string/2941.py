word = input()
c_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
result = len(word)
for i in c_word :
  if i in word :
    cnt = word.count(i) if i != "z=" else word.count(i)-word.count("dz=") #z=가 dz=까지 세지 않도록
    result -= 1*cnt if i != "dz=" else 2*cnt
print(result)