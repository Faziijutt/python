# define classes


# def add(a,b):
#     n=a+b
#     print(n)
# def mult(a,b):
#      return a*b  
# def greether(a,b):
#     if(a>b):
#         print("A is greather")
#     elif(a==b):
#         print("A and B is equal")
#     else:
#         print("B is greather")


# a=int(input("Enter 'A' number:"))
# b=int(input("Enter 'B' number:"))
# print("greather thn or egual")
# greether(a,b)
# print("Addition of A and B")
# add(a,b)
# print("multplication of A and B")
# n=mult(a,b)
# print(n)
# print("THANK YOU!")

# a=int(input("Enter 'A' number:"))
# b=int(input("Enter 'B' number:"))
# print("greather thn or egual")
# greether(a,b)
# print("Addition of A and B")
# add(a,b)
# print("multiplication of A and B")
# mult(a,b)
# print("THANK YOU!")

# c=int(input("Enter 'C' number:"))
# d=int(input("Enter 'D' number:"))
# print("greather then or egual")
# greether(c,d)
# print("Addition of C and D")
# add(c,d)
# print("multiplication of C and D")
# mult(c,d)
# print("THANK YOU!")

# print("a")
# print("b",end='')
# print("c")

# def add(n):
#     if(n==1):
#         return 1
#     return add(n-1)+n
# print(add(3))

# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)
# pattern(7)    

# def rem(word):
#     for item in list:
#         list.remove(word)
#         return list
# list=["faizan","umair","baker","fa"]  
# print(rem("fa"))  

n=int(input("ENTER THE TABLE NUMBER: "))
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
        
table(n)    

