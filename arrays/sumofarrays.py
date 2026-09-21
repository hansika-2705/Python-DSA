def sumofArray(a): 
  sum=0
  for i in a:
    sum=sum+i
  return sum
n=int(input())
a=[]
for i in range(n):
  ele=int(input())
  a.append(ele)
sum=0
for i in a:
  sum=sum+i
print(sum)
res=sumofArray(a)
print(res)
