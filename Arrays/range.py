def range_sum(a,st,end):
  return a[end]-a[st-1]
a=[3, 1, 4, 1, 5, 9, 2, 6]
prefix=prefixarray(a)
print(prefix)
print(range_sum(prefix,2,5))