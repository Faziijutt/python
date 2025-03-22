import random
'''
1 Stone
2 paper
3 sessior

'''
computer=random.choice([1, 2, 3])
n=str(input("ENTER THE ALPHABET(S for 'stone' , p for 'paper' , s for 'sessior'): "))
dict={"S":1,"p":2,"s":3}
revers_dict={1:"Stone",2:"paper",3:"sessior"}



if n not in dict:
    print("Plese! Enter alphabet in ('S','p','s')")

else:
    you=dict[n]

    print(f"You chose: {revers_dict[you]}\nComputer chose: {revers_dict[computer]}")

    if(computer==you):
        print("DRAW THE MATCH")     
    elif(computer==2 and you==3) or (computer==2 and you==1) or (computer==3 and you==1):
        print("YOU WON!")
    else:
        print("COMPUTER WON!")
           



