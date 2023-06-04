#Determine which number is bigger
#Ask the user for two numbers. If the inputs are not numeric, display an error message and exit the program. 
#If the inputs are numeric, check which number is bigger and print out an appropriate message to the user. Do also check if the numbers are equal.

print("*"*40)
print("ST2414 PSEC Practical 2 Qn 2")
print("*"*40)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

#Check if inputs are numeric value.
if not num1.isnumeric() or not num2.isnumeric():
    print("You did not enter a number!")
    exit()

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f"{num1} is bigger!")
elif num2 > num1:
    print(f"{num2} is bigger!")
else:
    print(f"{num1} and {num2} are the same!")
