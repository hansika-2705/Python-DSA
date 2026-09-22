def traversal(a):
  print('[',end="")
  for i in range(len(a)-1):
    print(a[i],end=", ")
  print(f'{a[-1]}]')
a=[1,2,3,4,5]
print(a)
traversal(a)