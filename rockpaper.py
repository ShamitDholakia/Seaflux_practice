
import random
win=0
while True:
    uinp = input("Enter a choice (rock, paper, scissors): ")
    choice = ["rock", "paper", "scissors"]
    rsp = random.choice(choice)
    if uinp == rsp:
        print("Its a tie!")
    elif uinp == "rock":
        if rsp == "scissors":
            print("You win!")
            win+=1
        else:
            print("You lose.")
    elif uinp == "paper":
        if rsp == "rock":
            print("You win!")
            win+=1
        else:
            print("ou lose.")
    elif uinp == "scissors":
        if rsp == "paper":
            print("ou win!")
            win+=1
        else:
            print("You lose.")
    list1=[uinp,rsp,win]
    with open("file2.txt","a") as file:
        file.write(str(list1))
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break