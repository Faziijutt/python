# class student:
#     fee=20000
#     sub="physics"
#     gender="male"
#     def __init__(self):     # dunder method whish is automatically called
#         print("i have crating init method")
#     def self_var(self):
#         print(f"the name is {self.name},the fee is {self.fee},the subject is {self.sub},the gender is {self.gender}")
    
#     @staticmethod  # without self variable
#     def self_not():
#         print("hello faizan")
# f=student()
# f.name="faizan"
# f.self_var()    # using self method

# # print(f"Name: {f.name}\n Fee: {f.fee}\n Subject: {f.sub}\n Gender: {f.gender}")    # using simple class

# f.name="umair"
# f.self_var()    # using self method

# # print(f"Name: {f.name}\n Fee: {f.fee}\n Subject: {f.sub}\n Gender: {f.gender}")    # using simple class 

# f.name="baker"  
# f.self_var()    # using self method

# # print(f"Name: {f.name}\n Fee: {f.fee}\n Subject: {f.sub}\n Gender: {f.gender}")    # using simple class

# f.self_not()    # without self variable



# # constructor program
# class student:
#     fee=20000
#     sub="physics"
#     gender="male"
#     def __init__(self,fee,sub,gender):     # dunder method whish is automatically called
#         self.fee=fee
#         self.sub=sub
#         self.gender=gender
#         print("constructor")

# f=student(50000,"math","male")
# print(f.gender,f.sub,f.fee)



# #PRACTISE SET
# class programmer:
#     company="Microsoft"
#     def __init__(self,name,salery,pin):
#         self.name=name
#         self.salery=salery
#         self.pin=pin
# obj=programmer("faizan",90000,1234)  
# print(obj.pin,obj.name,obj.salery,obj.company)   
# obj=programmer("umair",90000,8675)  
# print(obj.pin,obj.name,obj.salery,obj.company) 
# obj=programmer("baker",90000,7564)  
# print(obj.pin,obj.name,obj.salery,obj.company)  

 
# n=int(input("ENTER THE NUMBER: "))
# class calcul:
#     square=n*n
#     cube=n*n*n
#     squareroot=n**1/2

#     def __init__(self):
#         print(f"The cube is: {self.cube}\nThe square is: {self.square}\nThe squareroot is: {self.squareroot}")
# c=calcul()


from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
            print(f"ticket is book on train no: {self.trainNo} form {fro} to {to}")
    def getstatus(self):
            print(f"the train: {self.trainNo} is on running!")
    def getfare(self,fro,to) :
            print(f"ticket is fare in train no: {self.trainNo} form {fro} to {to} is {randint(222,999)}")     
t=train(1234)
t.book("FSD","LAHORE")
t.getstatus()
t.getfare("FSD","LAHORE")

