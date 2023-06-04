marks = [88, 74, 69, 90, 42, 79, 66, 73, 100, 99]

def menu():
    choice=" "
    while len(choice)!=0:
        print("\n+++ Welcome to the Marks Entry Simple System (MESS) +++")
        print(f"Current marks for {len(marks)} students stored in system.\n {marks}")
        print("1. Entry of marks to the MESS")
        print("2. Display the maximum mark in the MESS")
        print("3. Display the marks sorted in ascending order")
        print("4. Display a subset of marks in the MESS\n")
        choice=input("Pls choose 1-4 or press ENTER to quit: ")

        if choice.strip()=="1":
            entry()
        elif choice.strip()=="2":
            max_marks()
        elif choice.strip()=="3":
            sort_marks()
        elif choice.strip()=="4":
            edit_list()
  
    print("Thank you for making a MESS!")

def entry():
    global marks
    marks=[]
    i,mark=0,0
    while mark>=0:
        try:
            mark=eval(input(f"Pls enter marks for student {i+1} or -1 to end: "))
            if (mark<0 or mark>100):
                raise Exception("Pls enter a valid integer from 0-100.")
            marks.append(mark)
            i+=1
        except:
            print("Invalid input! Pls enter a valid integer from 0-100.")

def sort_marks():
    print(f"Marks in ascending order: {sorted(marks, reverse=False)}")

def max_marks():
    print(f"Highest Mark: {max(marks)}")

def edit_list():
    print(f"\nThe current set of marks stored in system is \n{marks}")
    print("Pls choose how you want to edit the list: ")
    print("1. Splice the list ")
    print("2. Remove a mark from the list")
    print("3. Change a mark")
    print("4. Add new marks")

    choice=input("Pls choose how you want to edit the list: ")
    if choice.strip()=="1":
            splice()
    elif choice.strip()=="2":
            remove()
    elif choice.strip()=="3":
            change()
    elif choice.strip()=="4":
            add()

def splice():
#    global marks

    print(f"\nThe current set of marks stored in system is \n{marks}")
    start=eval(input("Input start index to subset: "))
    end=eval(input("Input end index to subset: "))
    
    splice = marks[start:end]
    print(f"Your new marks set is {splice}")
#    marks=splice
#    print(marks)

def remove():
    temp = marks

    print(f"\nThe current set of marks stored in system is \n{marks}")
    start=eval(input("Input index to remove: "))
    del(temp[start])
    print(temp)

def change():
    temp = marks

    print(f"\nThe current set of marks stored in system is \n{marks}")
    start=eval(input("Input index to change: "))
    new=eval(input("Input new value: "))

    temp[start]=new
    print(temp)

def add():
    temp = marks

    print(f"\nThe current set of marks stored in system is \n{marks}")
    new=eval(input("Input new value: "))

    temp.append(new)
    print(temp)

menu()
