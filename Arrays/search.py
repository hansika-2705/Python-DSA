def search(a,el):
  c=0
  for i in a:
    if el==i:
      c=c+1
  return c
n=int(input())
a=list(map(int,input().split()))
ele=int(input())
#search(a,ele)
print(search(a,ele))