def roll(dice):
    while dice==1:
        b=int(input("press 1 or 0"))
        if b==1:
            print("roll")
        if b==0:
            return "exit"   
a=int(input("press 1 to roll and 0 to exit"))
roll(a)
    




