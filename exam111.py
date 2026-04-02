english = int(input("Enter the marks for the english:"))
maths = int(input("Enter the marks for the maths:"))
ai = int(input("Enter the marks for the ai:"))
total = english+maths+ai
percentage = (total/300)*100
print("Your percentage:",percentage)
if(percentage>40.0 and percentage<50.0):
    print("Your grade is E")
elif(percentage>50.0 and percentage<60.0):
    print("Your grade is D")
elif (percentage>60.0 and percentage<70.0):
    print("Your grade is C")
elif(percentage>70.0 and percentage<80.0):
    print("Your grade is B")
elif(percentage>80.0 and percentage<90.0):
    print("Your grade is A")
else:
    print("Your grade is S")
if(percentage>40.0):
    print("You are pass")
else:
    print("You are failed")