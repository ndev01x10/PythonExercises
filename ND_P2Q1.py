#Prompt user repeatedly to enter a number, or “Q” to quit. Compute the average of all the numbers entered by the user until “Q” is entered, after which you are to display the computed average, to 2 decimal places.
print("*" * 40)
print("ST2414 PSEC Practical 2 Submission 1")
print("*" * 40)

total = 0
count = 0
user_input = input("Please enter a number or 'Q' to stop: ") # Gets input from the user

while user_input != 'Q' and user_input != 'q':
    if user_input.isnumeric(): #Checks whether the input is numeric then converts the value
        total += int(user_input)
        count += 1
        print(f"Current total of {count} values is {total}")
    else:
        print("You did not enter a number!") #Prompts the user that they did not enter a valid number
    user_input = input("Please enter a number or 'Q' to stop: ") #Input is obtain again in order to break the loop, otherwise, it will go into infinite loop

if count > 0:
    average = total / count
    print(f"The average of {count} numbers is: {average:.2f}") #Prints the outcome in 2 decimal places
else:
    print("No valid numbers entered.")
