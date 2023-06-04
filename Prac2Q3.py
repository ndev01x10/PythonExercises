#Using nested if-else. Company X revises the increment to the salary of a staff based on the following criteria. For example, if a staff has worked for less than 10 years and is earning a salary of $1999, he would get an increment of $20.
#Write a Python program that will prompt for 2 numbers which represent years of service and salary of a staff. The program will then display the increment of the staff. As before, do the necessary checks for numeric inputs.

print("*"*40)
print("ST2414 PSEC Practical 2 Qn 3")
print("*"*40)

service = input("Enter number of years in service: ")
salary = input("Enter current salary: ")

#Check if inputs are numeric value.
if not service.isnumeric() or not salary.isnumeric():
    print("You did not enter a number!")
    exit()

service = int(service)
salary = int(salary)

increment = 0

if service < 10 and salary < 1000:
    increment = 100
elif service < 10 and salary < 2000:
    increment = 200
elif service < 10 and salary >= 2000:
    increment = 300
elif service >= 10 and salary < 1000:
    increment = 200
elif service >= 10 and salary < 2000:
    increment = 300
else:
    increment = 400

new_salary = salary + increment

print(f"Your increment is ${increment}")