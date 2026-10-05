#returning 1 index
def linearsearch(a,el):
    for i in range(len(a)):
        if a[i]==el:
            print(f'{el} is found at {i} index')
            a.append(i)
    return -1
a=[12,2,44,23,14,65]
linearsearch(a,14)
#returning multiple index
def linearsearch(a,el):
    ar=[]
    for i in range(len(a)):
        if a[i]==el:
            print(f'{el} is found at {i} index')
            ar.append(i)
    return ar
a=[12,2,44,23,14,65,14]
print(linearsearch(a,14))