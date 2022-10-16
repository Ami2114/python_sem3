
import imp


import math

# 1. Triple all the numbers given in list

a=(12,19,20,35,40,59)

def multiply(x):
    return x*x*x

num=map(multiply,a)
print(list(num))

# 2. Separate even odd number from given list

def number(a):
    if a % 2 == 0: 
        return a,("even")
    else :
        return a,("odd")
res=map(number,a)
print(list(res))

# 3.Print all string in lower case from given tuple

str=("ABC","ZYX","IJK")

def lower_case(str):
    return str.lower()

str2=map(lower_case,str)
print(tuple(str2))

# 4.Print square root of numbers given in list

def sqrt(i):
    return math.sqrt(i)

sqrt_=map(sqrt,(4,9,16,55))
print(list(sqrt_))

# 5.Eliminate duplicate letter from given string

list1=[12,22,34,55,22,12]

def dup_letter(x):
        if x not in list1:
            return True
        else:
            return False

result=map(dup_letter,list1)
print(list(result))

# 6.Print table of any number (Error)

num2=(input("Enter any number: "))
b=[1,2,3,4,5,6,7,8,9,10]
def table(num2,b):
    return num2*b

res2=map(table,num2,b)
print(list(res2))

# 7.

list_1=[1,2,3,4,5]
list_2=[31,55,94,67,2]
print("Original list:")
print(list_1)
print(list_2)
res3 = map(lambda x, y: x + y, list_1, list_2)
print("Result: ")
print(list(res3))

#  8.

def float(k):
    return int(k)

result_=map(float,(1.2,22.2,1001.9,4.1))
print(list(result_))

# 9

num3=(1,2,3,4,5,6,7,8,9)
list_3=list(reversed(num3))
print(list_3)


#  10 (Error)
dict=(input("enter a name: "))
res4=map(lambda i:(i[0]+"@gmail.com"),dict)
print(dict(res4))