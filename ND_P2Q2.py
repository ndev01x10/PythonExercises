#Prompt user for a starting number and an ending number then display all the odd numbers in between using a for loop, separated by tab (“\t”). Should the first number be bigger than the second number, you should display the output in reverse.
#Hint: you should use the step parameter to do this

print("*" * 40)
print("ST2414 PSEC Practical 2 Submission 2")
print("*" * 40)

start_num = int(input("Please enter the starting number: "))
end_num = int(input("Please enter an ending number: "))

count = 0  #Counter variable for tracking the number of odd numbers found

if start_num <= end_num:
    for num in range(start_num, end_num + 1):
        if num % 2 != 0:
            print(num, end="\t")
            count += 1  #Increment the counter by 1

            if count == 5:  #Check if 5 odd numbers have been printed
                break  #Exit the loop if 5 odd numbers have been printed

else:
    for num in range(start_num, end_num - 1, -1):
        if num % 2 != 0:
            print(num, end="\t")




        

