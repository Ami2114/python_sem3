# 1.

num=(1,-4,2,6,-15,9)

def negative(num):
    if num<0:
        return num
    else:
        return False

res=filter(negative,num)
print(list(res))

# 2.

num2=(12,2,15,99,67)

def odd_num(num2):
    if num2 % 2 != 0:
        return num2
    else:
        return False

res2=filter(odd_num,num2)
print(list(res2))

# 3.

letters=('a','b','c','d','E','I','j','o')

def lower(letters):
    return letters.lower()

def filter_vowels(letters):
    vowels=['a','e','i','o','u']
    return True if letters in vowels else False

filtered_vowels= filter(filter_vowels,letters)
vowels=list(filtered_vowels)
print(vowels)

# 4. 

NumList = [0,1,2,-3,4,-6,-7,8,3,-10]

posInts = list(filter(lambda x: True if x>0 else False, NumList))

print("Positive integers in the list: ", posInts)

#  5

Change = list(filter(lambda x: x>0 ,map(lambda x: x*-1,NumList)))

print("The Changed list: ", Change)
