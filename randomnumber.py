import random
numg=random.randint(1,100)
count=0
while numg:
    for i in range(0,5):
        uinput=int(input("Enter a number"))
        if uinput>numg:
            print("number is to high")
        elif uinput<numg:
            print("number is low")
        elif uinput==numg:
            print("correct guess at:",count)
        count+=1
    print("try again")
    break