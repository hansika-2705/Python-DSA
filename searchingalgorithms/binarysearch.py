def binarysearch(a,el):
  l=0
  r=len(a)
  while l<r:
    m=(l+r)//2
    if a[m]==el:
      return m
    elif a[m]<el:
      l=m
    else:
      r=m    
a=[6,7,11,14,17,20]
print(binarysearch(a,17))