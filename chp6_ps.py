# problem 1

a=int(input("Enter number A:"))
b=int(input("Enter number B:"))
c=int(input("Enter number C:"))
d=int(input("Enter number D:"))


if(a>b and a>c and a>d):
    print("greterthen is",a)
elif(b>a and b>c and b>d):
    print("greterthen is",b)
elif(c>a and c>b and c>d):
    print("greterthen is",c)
elif(d>a and d>b and d>c):
    print("greterthen is",d)        


# problem 2

marks1=int(input("Enter number of sunbject 1:"))
marks2=int(input("Enter number of sunbject 2:"))
marks3=int(input("Enter number of sunbject 3:"))

total_percentage=((100)*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed:",total_percentage)
else:
    print("you failed:",total_percentage)    


# problem 3

p1="Make a lot of money"
p2="Buy now"
p3="Subcri"
p4="click this"

message=(input("Enter comment:"))

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("this comment is spam")
else:
    print("this comment is not a spam")    


# problem 4

name=str(input("Enter your name:"))

if(len(name)<10):
    print("your name is less then 10 charecter")
else:
    print("your name is more then 10 charecter")


# problem 5

list=["Faizan","rohan","Riaz","umair"]

name=str(input("Enter your name:"))

if(name in list):
    print("your name is in the list")
else:
     print("your name is not in the list")  


# problem 6

number=int(input("Enter your number :"))

if(number<=50):
    print("your grade is F")
elif(number<=60):
    print("your grade is D") 
elif(number<=70):
    print("your grade is C")
elif(number<=80):
    print("your grade is B")
elif(number<=90):
    print("your grade is A")            
elif(number<=100):
    print("your grade is Ex")    


# problem 7

post=(input("Enter your post:"))

if("Faizan" in post.capitalize()):
    print("This post is about Faizan")
else:
    print("This post is not about Faizan")    