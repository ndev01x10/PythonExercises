#Define in a Python script, a main() function to loop to display a menu
#Define functions F1 to F4 to process the choices 1-4. You may copy the codes from Q1, Q2, Q4 and Q5. In the main function, check the user’s input to call upon the appropriate functions.

def main():
    while(True):
        print("*"*40)
        print("ST2414 PSEC Practical 2 Qn 7")
        print("*"*40)
        print("1. Determine odd or even")
        print("2. Determine bigger number")
        print("3. Find sum of numbers")
        print("4. Display even numbers")
        print("****************************************")

        a = input("Enter a choice: ")
        if a=="1":
            Q1()
        elif a=="2":
            Q2()
        elif a=="3":
            Q3()
        elif a=="4":
            Q4()
        else:
            break

def Q1():
    a = input("Enter a number: ")
    if (not a.isnumeric()):
        print("You did not enter a number")
    else:
        if (eval(a)%2==0):
            print(f"{a} is even")
        else:
            print(f"{a} is odd")

def Q2():
    a = input("Enter a number: ")
    if not a.isnumeric():
        print("You did not enter a number")
    else:
        b = input("Enter another number: ")
        if (not b.isnumeric()):
            print("You did not enter a number")
        elif (eval(a)==eval(b)):
            print(f"{a} and {b} are the same!")
        elif (eval(a)>eval(b)):
            print(f"{a} is bigger!")
        else:
            print(f"{b} is bigger!")
        
def Q3():
    sum=0
    a=input("Pls enter a number or Q to stop: ")
    while a!='Q' and a.isnumeric():
        sum+=eval(a)
        print(f"Current total is {sum}") 
        a=input("Pls enter a number or Q to stop: ")

    else:
        if a!='Q':
            print('Pls enter a valid number!')
        else:
            print(f'Final sum is {sum}')

def Q4():
    a=input("Pls enter a starting number: ")
    b=input("Pls enter an ending number: ")
    if a.isnumeric() and b.isnumeric():
        for x in range(eval(a), eval(b)):
            if(x%2==0):
                print(x,end="\t")
    else:
        print('Pls enter valid numbers!')

main()
print("Thank you!")