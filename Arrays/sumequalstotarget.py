def sumarray(a,k,target):
  s=0
  if k<=0 or k>len(a):
    return 'invalid key elements'
  for  i in range(k):
    s+=a[i]
  if s==target:
    return [a[i] for i in range(k)]
  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]
    if s==target:
      return [a[i] for i in range(i-k+1,i+1)]
  return -1    
a=[1,2,3,4,5]
print(sumarray(a,3,10))