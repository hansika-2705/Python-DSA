def remove(string):
  for ch in string:                                                                  
    if  ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' :
      string=string.replace(ch,"")
  return string
string=input()
result=remove(string)
print(result)