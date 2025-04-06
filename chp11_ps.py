# # PRACTISE SET
# class A:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
            
# class B(A):
    
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#         print(f"the vector A is {self.i}i and {self.j}j")
#         print(f"the vector B is {self.i}i and {self.j}j and {self.k}k") 
# a=A(1,2)
# b=B(1,2,3)        


# class employe:
#     sallary=350
#     increment=30
    
    
#     @property
#     def increm(self):
#         return (self.sallary +self.sallary*(self.increment/100))
    
#     @increm.setter
#     def increm(self,sallary):
#         self.increment=((sallary/self.sallary)-1)*100
# c=employe()  
# c.increm=390
# print(c.increment)


class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}i"
c1=complex(2,4)    
c2=complex(5,6)    
print(c1 + c2)

