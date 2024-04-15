#This is the Second Task of the Python Programming in which i had to create Calculator which performs Operations Based on User's Choice
#This Program is tested for Various Inputs.

a=int(input("Enter the Number: "))
c=str(input("Enter the Operand: "))
b=int(input("Enter the Second Number: "))
if c=="+":
    print("Result is",end=" ") 
    print(a+b)
elif c=="-":
    print("Result is",end=" ") 
    print(a-b)
elif c=="*":
    print("Result is",end=" ") 
    print(a*b)
elif c=="/":
    print("Result is",end=" ") 
    print(a/b)
elif c=="%":
    print("Result is",end=" ") 
    print(a%b)
elif c=="//":
    print("Result is",end=" ") 
    print(a//b)
elif c=="**":
    print("Result is",end=" ") 
    print(a**b)
else:   
    print("Invalid Operator")

