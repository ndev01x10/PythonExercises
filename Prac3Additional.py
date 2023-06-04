order=[]

def main():
    #Part 1, get input
    s = "Beef Curry, Curry Prata, Kimchi Fried Rice, Katsu Curry" #Input("Please enter your favourite dishes, separated by comma ','\n")
    dishes = s.split(sep=",") #Can use strip() to remove whitespaces
    choice=" "
    #print(dishes)

    #Part 2, service
    while len(choice)>0:
        choice = input("\n\nPlease input food to search: ")
        if len(choice)==0:
            break 

        matches=[]

        for dish in dishes:
            if dish.lower().find(choice.lower())>=0:
                matches.append(dish.strip())
                
        if len(matches)==0:
            print(f"Sorry, we don't serve {choice}!\nPls choose from {dishes}")
            choice=input("Please press ENTER key to quit or 'N' enter new search: ")
        else:
            addOrder(matches)
            #Break
    num=len(order)
    if num>0:
        print(f"You have ordered {num} items. Pls wait for up to {num*5} minutes.")
    print("Thank you for using SP Automated Menu System (SPAMS)")
        
def addOrder(matches):
    submenu=""
    i=1
    for dish in matches:
        submenu+=f"\n{i}. {dish}"
        i+=1

    print(f"Yes, we serve the following:{submenu}")
    choice=-1
    while (choice)!=0:
        choice=0 #Indicate exit case
        choice=eval(input(f"Enter the dish 1-{i-1} that you would like to order, or 0 to stop: "))
        if choice>=0 and choice<i:
            if choice>0:
                order.append(matches[choice-1])
                print(f"{choice} added")
           #print(order)
        else:
            print(f"Invalid choice! Pls enter 1-{i-1} or 0 to stop")

    #Outside while means finish ordering
    print(f"You have ordered {order}")
main()
