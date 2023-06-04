#Using try-catch instead of isnumeric()
#Redo Practical 2 questions 1-3 using try-except instead of the isnumeric()

print("****************************************")
print("ST2414 PSEC Practical 2b Qn 1")
print("****************************************")

a = input("Enter a number: ")
try:
    if (eval(a)%2==0):
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
except:
        print("You did not enter a number")

