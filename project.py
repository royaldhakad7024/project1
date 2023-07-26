import random
l=["rock","paper","scissors"]
print("""option:
      1-rock
      2-paper
      3-scissors
      """)
us=0
cs=0
tie=0
while True:
    uc=int(input("""Game Start...
                 1 Yes
                 Press any number | Exit
                 """))    
    if uc==1:
        userInput=int(input("""
                            1 Rock🤜
                            2 Paper🖐
                            3 Scissors✌️
                            """))
        if userInput==1:
            uchoice="rock"
        elif userInput==2:
            uchoice="paper"
        elif userInput==3:
            uchoice="scissors"   
        cchoice=random.choice(l)
        if uchoice==cchoice:
            print("Computer💻 Value=",cchoice)
            print("User👨‍🏭 Value=",uchoice)
            print("Game Draw🥳✨")
            tie+=1
            # print("tie score is=",tie)
            # print("user score is=",us)
            # print("computer score is=",cs)
        elif (uchoice=="rock" and cchoice=="scissors") or (uchoice=="paper" and cchoice=="rock") or (uchoice=="scissors" and cchoice=="paper"):
            print("Computer💻 Value=",cchoice)
            print("User👨‍🏭 Value=",uchoice)
            print("You Win🥳✨")
            us+=1
            # print("tie score is=",tie)
            # print("user score is=",us)
            # print("computer score is=",cs)
        else:
            print("Computer💻 Value=",cchoice)
            print("User👨‍🏭 Value=",uchoice)  
            print("Computer Win🥳✨")
            cs+=1
            # print("tie score is=",tie)
            # print("user score is=",us)
            # print("computer score is=",cs)

    else:
        break     
print("tie score is=",tie)
print("user score is=",us)
print("computer score is=",cs)
if us>cs:
    print("final winner is user🥳")
elif cs>us:
    print("final winner is computer😱")  
else:
    print("tie👔")
