#Part 1, get input
s = input("Please enter your restaurant dishes, separated by comma ','\n")
dishes = s.split(sep=",") #Can use strip() to remove whitespaces
#print(dishes)

#Part 2, service
choice = input("Please input food to search: ")
matches=""

for dish in dishes:
    if dish.lower().find(choice.lower())>=0:
        matches+="\n"+dish.strip()
        
if len(matches)>0:
    print(f"Yes, we serve the following:{matches}")
else:
    print(f"Sorry, we don't serve {choice}!\nPls choose from {dishes}")


    