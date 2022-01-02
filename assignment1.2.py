print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6.exponentiation")
print("7.floor division")

choice=int(input("enter your choice:"))
num1=int(input("enter first no."))
num2=int(input("enter second no."))
if(choice==1):
   print("addition of two numbers=",num1+num2)
elif(choice==2):
   print("subtraction of two numbers=",num1-num2)
elif(choice==3):
   print("multiplication of two numbers=",num1*num2)
elif(choice==4):
    print("division of two numbers=",num1/num2)
elif(choice==5):
    print("modulus of two numbers=",num1%num2)
elif(choice==6):
    print("exponentiation of two numbers=",num1**num2)
else:
    print("floor division of two numbers=",num1//num2)
