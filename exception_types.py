num = ["128","34","69","5"] #List of strings
num1 = [128,33,44,65] #List of integers
num2 = [True,False,True, True] #List of booleans
num3 = ("128","34","69","5") #Tuple of strings
num4 = (32,99,43,77) #Tuple of integers
num5 = (True,False,False,True) #Tuple of booleans
students = {"Nora": 15, "Gino": 30} #Dictionary

#IndexError exception

try:
    print(num[99])
    print(num1[99])
    print(num2[99])
    print(num3[99])
    print(num4[99])
    print(num5[99])
except IndexError:
    print("Index is completely out of range")

#KeyError exception
print(students["Marc"])

#NameError exception; b is not defined!

print(num1 * 4 * b)

print(num98 * num99) #Neither num98 and num99 are defined! :(

#TypeError exception: Operation applied to an object of an inappropriate type.

a = 1/"x"
print(a)

#ZeroDivisionError: You cannot divide by zero!

b = 1/0
print(b)

#Blank except statement catches ALL exceptions!

try:
    a = num1/0
    b = num1 * 3
    print(a)
    print(b)
except:
    print("We can catch all exception in this block! No matter its nature or cause of error")