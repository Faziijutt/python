# # multiple inhertitence
# class A:
# # class A:      # multilevel inheritence
#     def __init__(self):
#        print("Constructor of A")
#     a=2
#     def aa(self):
#      print(f"the number is {self.a}")

# class B:
# # class B(A):   # multilevel inheritence
#     def __init__(self):
#        super().__init__()   # used for inherit constructor 
#        print("Constructor of B") 
#     b=4
#     def bb(self):
#      print(f"the number is {self.b}")

# class C:      
# # class C(B):    # multilevel inheritence
#     def __init__(self):
#        super().__init__()    # used for inherit constructor
#        print("Constructor of C")  
#     c=5
#     def cc(self):
#      print(f"the number is {self.c}")

# class D(A,B,C):
# # class D(C):    # multilevel inheritence  
#     def __init__(self):
#        super().__init__()    # used for inherit constructor
#        print("Constructor of D")  
#     d=6
#     def dd(self):
#      print(f"the number is {self.d}")

# obj=D()
# obj.aa()
# obj.bb()
# obj.cc()
# obj.dd()



class method:
    n=5
    name="faiz"
    @classmethod     # for mot change the class antribute
    def num(cls):
        print(f"The class antribute is {cls.n}  {cls.name}")
a=method()
a.name="faizan"
a.n=10
a.num()        