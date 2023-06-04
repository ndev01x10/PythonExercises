#Determine if a number is odd or even 
#Ask the user for a number. If the input is not numeric, display an error message and exit the program. Hint: use the isnumeric() string function. If the input is numeric, check if the number is even or odd and print out an appropriate message to the user. 
#Hint: Use the % modulus operator which gives the remainder when a number x is divided by another number y.

print("*"*40)
print("ST2414 PSEC Practical 2 Qn 1")
print("*"*40)

num = input("Enter a number: ")

if (not num.isnumeric()):
    print("You did not enter a number!")
else:
    if (int(num)%2==0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")