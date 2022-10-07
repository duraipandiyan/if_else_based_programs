s1=int(input("enter the TAMIL MARK="))
s2=int(input("enter the ENGLISH MARK="))
s3=int(input("enter the MATHS MARK="))
s4=int(input("enter the PHYSICS MARK="))
s5=int(input("enter the CHYMISTRY MARK="))
avg=s1+s2+s3+s4+s5/5
print("avrge is",avg)
if avg>90:
    print("A GRADE")
elif  avg>80 and avg<=90:
    print("B GRADE")
elif avg>70 and avg<=80:
    print("C GRADE")
elif avg>60 and avg<=70:
    print("D GRADE")
else:
    print("sorry fail")


print("it will be run sucessfully ")