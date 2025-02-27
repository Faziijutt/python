
# problem 1

a=str(input("Enter your name:"))
print(f"good afternoon {a}")

# problem 2
Letter='''
          Dear <|name|>
          You are selected!
          <|date|>'''
print(Letter.replace("<|name|>","Faizan").replace("<|date|>","6/3/2005"))

# problem 3
a="Faizan   is a   good    boy"
print(a.find("   "))

# problem 4
a="Faizan   is a   good    boy"
print(a.replace("   "," "))
 
#  problem 5
a="Dear Faizan,\n\t This Phython course is nice.\nThanks"
print(a)