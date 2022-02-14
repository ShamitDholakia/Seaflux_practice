import random 
x = "1"
while x == "1":
    no = random.randint(1,6)
    if no == 1:
        print("*")
    if no == 2:
        print("* * ")
    if no == 3:
        print("* * *")
    if no == 4:
        print("* * * *")
    if no == 5:
        print("* * * * *")
    if no == 6:
       print("* * * * * *")
         
    x=input("press 1 to roll again and 0 to exit:")
    print("\n")
