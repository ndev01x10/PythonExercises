#Create dictionary
services={}

#Get input eg SMTP:25|HTTP :80|HTTPS: 443|FTP:20| SSH:22|TELNET:23
s = input("Please enter service:port that were found to be open, separated by '|'\n")
pairs = s.split(sep="|") #Can use strip() to remove whitespaces
#print(pairs)

#Split into service and port
#Choice = input("Please input port number for your 'service': ")
for pair in pairs:
    svc=pair.split(':')
    services[svc[0].strip()]=int(svc[1].strip())

#print(services)
print("\nThese are the open ports found and their corresponding services:")
for service, port in services.items():
	print(f"{port}:{service}")

#a)Search for service or port
s = input('''
1) Search for open port
2) Search for service running
3) Update dictionary
Please enter request:''')

if s=='2':
    s=input('Enter service: ').upper()
    print(f'{s} is running on port {services[s]}')
elif s=='1': #Implement search
    s=input('Enter port: ')
    print(f'No service is running on port {s}')
elif s=='3': #Implement update
    s=input('Enter service:port: ')
    print(services)
