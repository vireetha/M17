weight = float(input("Enter your weight in kilograms: "))  
height_cm = float(input("Enter your height in centimeters: "))  

# Calculate BMI
bmi = weight / ((height_cm / 100) ** 2)  

if bmi < 18.5:
    print("You are classified as: Underweight")

if 18.5 <= bmi < 25: 
    print("You are classified as: Normal weight")

if 25 <= bmi < 30:  
    print("You are classified as: Overweight")

if bmi >= 30:  # BMI is 30 or greater
    print("You are classified as: Obesity")
