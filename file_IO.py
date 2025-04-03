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

# a=open("poem.txt")
# content=a.read()
# if("Twinkle" in content):
#     print("The word twinkle is in the content")
# else:    
#     print("The word twinkle is not in the content")
# a.close()    


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

n=int(input("ENTER THE NUMBER: "))
def generatetable(n):
    table=""
    for i in range(1,11):
        table +=f"{n}*{i}={n*i}\n"
    with open(f"tables/table_{n}","w")  as f:
      f.write(table)  

for i in range(2,21):
    generatetable(i)