#Write a Python program that prompts the user to enter the length of a square and prints out the area and perimeter of the square.
#Hint -- > Remember to convert your inputs to datatype int or float before performing calculations!

#Notes: Area of Square = a x 2, a = sides of the square.
#Notes: Perimeter of Square = a x 4, a = sides of the square, add all four sides of the square or by multiplying any one side by 4. The formula to find perimeter of a square is (4 × side) units.

length = eval(input('Please enter the length of the square: '))

print(f'The Area of the square is: {length*length}')
print(f'The Perimeter of the square is: {2*(length+length)}')
