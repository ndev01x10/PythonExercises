#While loops for user’s inputs.
#Prompt user repeatedly to enter a number, or “Q” to quit. Sum each number entered by the user until “Q” is entered, after which you are to display the total of all the numbers entered. 

print("*"*40)
print("ST2414 PSEC Practical 2 Qn 4")
print("*"*40)

total = 0
user_input = input("Please enter a number or 'Q' to stop: ")

while user_input!='Q' and user_input!='q':
    if user_input.isnumeric():
        total+=eval(user_input)
        print(f"Current total is {total}")
    else:
        print("You did not enter a number!")
    user_input = input("Please enter a number or 'Q' to stop: ")
    
print(f"The final sum is: {total}")