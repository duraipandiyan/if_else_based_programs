str="The quick Brown Fox"
c1=0
c2=0
for i in str:
    if i.islower():
        c1=c1+1
    elif i.isupper():
        c2=c2+1
print("the lower case is ")
print(c1)
print("the upper  case is ")
print(c2)


