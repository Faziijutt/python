# # read the file
# a=open("file.text")
# print(a.read())
# a.close()


# a=open("file.text")
# b=a.readline()
# while(b!=""):
#     print(b)
#     b=a.readline()
# a.close

# with open("file.text") as a:
#     print(a.readline())

# # write in the file
# b="HELLO WORLD 000"
# a=open("myfile.text","w")
# a.write(b)
# a.close()



# PRACTISE SET

# find the word in the file
# a=open("poem.txt")
# content=a.read()
# if("Twinkle" in content):
#     print("The word twinkle is in the content")
# else:    
#     print("The word twinkle is not in the content")
# a.close()    

# generated the score
# import random
# def game():
#     print("you playing the game . . . ")
#     score=random.randint(1,100)
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#     if(hiscore!=""):
#         hiscore=int(hiscore)
#     else:
#          hiscore=0     
#     print(f"your score: {score}") 
#     if(score>hiscore):
#       with open("hiscore.txt","w") as f:
#          f.write(str(score))
         
#     return score

# game()

# n=int(input("ENTER THE NUMBER: "))
# print(f"you entered: {n}")
# def generatetable(n):

# #  generated the file in folder in which table are genrated who you enterd the integer number
#  with open(f"tables/tab_{n}","w") as f:
#    for i in range(1,11):
#     k=f"{n}*{i}={n*i}\n"
#     f.write(k)

# generatetable(n)

# word convert to "####"
# word=["donkey","grate","animal"]
# a=open("file.text")
# b=a.read()
# for n in word:
#  c=b.replace(n,"#####")
# a=open("file.text","w")
# b=a.write(c)

# blank the file
# a=open("hiscore.txt")
# b=a.read()
# c=open("hiscore.txt","w")
# c.write("")