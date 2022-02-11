weight=int(input("Enter Your weight"))
height=int(input("enter your height"))
bmi=(weight*100)/height
list1=[weight,height,bmi]
print(list1)
with open("myfile.txt","w") as file:
    for i in list1:
        file.write(str(i))
        file.write("\n")
        
if bmi<18.5:
    print("underweight")
elif(bmi>=18.5 and bmi<25):
    print("normal")
elif bmi>=25 and bmi<30:
    print("oveweight")
else:
    print("obesity")