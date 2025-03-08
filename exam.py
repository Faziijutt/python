def feb(n):

    if(n==1):
        return(1)
    elif(n==0):
        return 0
    else:
        return feb(n-1)+feb(n-2)
print(feb(5))

def series(tera):
    if term <= 1:
        return term
    else:
        return series(term-1) + series(term-2)
for i in range(3):
    print(series(i))

def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)
print(fac(7))


# def add(a,b):
#     n=a+b
#     print(n)
# def greether(a,b):
#     if(a>b):
#         print("a is greather")
#     else:
#         print("b is greather")

# a=7
# b=7
# greether(a,b)
# add(a,b)
# c=4
# d=2
# greether(c,d)
# add(c,d)
