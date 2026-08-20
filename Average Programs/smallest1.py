a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))

if b>a and c>b:
    print("a is smallest")
elif a>b and c>b:
    print("b is smallest")
else:
    print("c is smallest")    