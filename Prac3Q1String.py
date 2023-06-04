#part 1, get input
s = input("Please enter ports that were found to be open '|'\n")
ports = s.split(sep="|") #Can use strip() to remove whitespaces
#print(dishes)

#Part 2, service
choice = input("Please input port number for your 'service': ")
for port in ports:
    if port.strip()==choice.strip():
        print(f"Yes, port {choice} is open!") 
        break
else:
    print(f"Sorry, port {choice} is closed! Pls choose from {ports}")


    