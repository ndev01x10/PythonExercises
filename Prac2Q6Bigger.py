#Using try-catch instead of isnumeric()
#Redo Practical 2 questions 1-3 using try-except instead of the isnumeric()

print("****************************************")
print("ST2414 PSEC Practical 2 Qn 3")
print("****************************************")

try:
    a = input("Enter number of years in service: ")
    year = eval(a)
    b = input("Enter current salary: $")
    salary = eval(b)
    if year<10:
            if salary<1000:
                increment = 100
            elif salary < 2000:
                increment = 200
            else:
                increment = 300
    else: # 10 or more years
            if salary<1000:
                increment = 200
            elif salary < 2000:
                increment = 300
            else:
                increment = 400
    print(f"Your increment is {increment}")
except:
    print("You did not enter a valid number")