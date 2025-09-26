# Code to check BMI (body mass index) calc
# BMI = Weight (kg) / [Height]^2

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

height = height / 100
bmi = weight / height ** 2

print(f"The BMI is {bmi}")