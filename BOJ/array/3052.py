list = []
mod_list = []

list.append(int(input()))
mod_list.append(list[0] % 42)

for i in range(1, 10) :
  list.append(int(input()))
  mod_list.append(list[i] % 42)
  for j in range(len(mod_list)-1) :
    if mod_list[j] == list[i] % 42 :
      mod_list.pop()
      break

print(len(mod_list))