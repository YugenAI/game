import random
a=input("Do you want to play rock paper scissors ? ")
choices=["rock","paper","scissors"]
if a=="yes"or a=="YES" or a=="Y" or a=="y":
    choices=["rock","paper","scissors"]
    b=input("what is your choice [rock or paper or scissor] ? ").lower()
    if b=="rock" :
        c= random.choice(choices)
        if c=="rock" :
            print("i chose "+c)
            print("draw")
        else:
            if c=="paper":
                print("i chose " + c)
                print("I win")
            else:
                if c=="scissor":
                    print("i chose " + c)
                    print("you win")
    elif b=="paper" :
            c= random.choice(choices)
            if c=="rock" :
                print("i chose " + c)
                print("you win")
            else:
                if c=="paper":
                    print("i chose " + c)
                    print("draw")
                else:
                    if c=="scissor":
                        print("i chose " + c)
                        print(" i won ")
    elif b=="scissor" :
         c = random.choice(choices)
         if c == "rock":
             print("i chose " + c)
             print("i won")
         else:
             if c == "paper":
                 print("i chose " + c)
                 print("you won")
             else:
                 if c == "scissor":
                    print("i chose " + c)
                    print(" draw ")
    else:
        print("wrong option")
    d=input("Do you want to play again ? ")
    if d=="yes"or d=="YES" or d=="Y" or d=="y":
        choices = ["rock", "paper", "scissor"]
        b = input("what is your choice [rock or paper or scissor] ? ").lower()
        if b == "rock":
            c = random.choice(choices)
            if c == "rock":
                print("i chose " + c)
                print("draw")
                print("thank you for playing again")
            else:
                if c == "paper":
                    print("i chose " + c)
                    print("I win")
                    print("thank you for playing again")
                else:
                    if c == "scissor":
                        print("i chose " + c)
                        print("you win")
                        print("thank you for playing again")
        elif b == "paper":
            c = random.choice(choices)
            if c == "rock":
                print("i chose " + c)
                print("you win")
                print("thank you for playing again")
            else:
                if c == "paper":
                    print("i chose " + c)
                    print("draw")
                    print("thank you for playing again")
                else:
                    if c == "scissor":
                        print("i chose " + c)
                        print(" i won ")
                        print("thank you for playing again")
        elif b == "scissor":
            c = random.choice(choices)
            if c == "rock":
                print("i chose " + c)
                print("i won")
                print("thank you for playing again")
            else:
                if c == "paper":
                    print("i chose " + c)
                    print("you won")
                    print("thank you for playing again")
                else:
                    if c == "scissor":
                        print("i chose " + c)
                        print(" draw ")
                        print("thank you for playing again")
        else:
            print("wrong option")
    else:
        if a == "no" or a == "NO" or a == "n" or a == "N":
            print("thankyou for you having a look on me")
        else:
            print("please give correct answers ")

else:
    if a=="no" or a=="NO" or a=="n" or a=="N":
        print("thankyou for you having a look on me")
    else:
        print("please give correct answers ")

