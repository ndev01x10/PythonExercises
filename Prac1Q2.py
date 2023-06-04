#Write a Python program that prompts the user to enter his height and weight, then calculates his BMI to a precision of 1 decimal place.
#Notes: BMI = weight (kg) / height2 (m).

weight = eval(input("Please enter your weight in kilograms: "))
height = eval(input("Please enter your height in meters: "))

bmi = weight / (height*height)

print(f"Your BMI is: {bmi:.3}")

