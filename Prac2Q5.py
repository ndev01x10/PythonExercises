#For loops for user’s inputs
#Prompt user for a starting number and an ending number then display all the even numbers in between using a for loop, separated by tab (“\t”)

print("*"*40)
print("ST2414 PSEC Practical 2 Qn 5")
print("*"*40)

start_num = int(input("Please enter a starting number: "))
end_num = int(input("Please enter an ending number: "))

count = 0  #Counter variable for tracking the number of even numbers found

for num in range(start_num, end_num + 1):
    if num % 2 == 0:
        print(num, end="\t")
        count += 1  #Increment the counter by 1

        if count == 5:  #Check if 5 even numbers have been printed
            break  #Exit the loop if 5 even numbers have been printed

