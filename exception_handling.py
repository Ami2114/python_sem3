# try: 
#     print("try block")
#     num1=int(input("Enter first number"))
#     num2=int(input("Enter second number"))
#     res=num1/num2
# except:
#     print("Except block")
#     print("Number1 is not divisible by 0")
# else:
#     print("Else block")
#     print("Output ",res)
# finally:
#     print("Exceptional Handling program")
try:
    age=int(input("Enter your age: \n"))
    if age<18:
        raise ValueError(age)
except ValueError:
    print(age," your age is not valid")
else:
    print(age,"Your age is valid")
finally:
    print("....")