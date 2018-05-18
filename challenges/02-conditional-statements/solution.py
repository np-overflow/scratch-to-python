# Ask for height
height = input('What is your height (cm)? ')
height = int(height) / 100 # Convert to m

# Ask for weight
weight = input('What is your weight (kg)? ')
weight = int(weight)

# Calculate BMI
bmi = weight / (height * height)

# Check the BMI status
if bmi < 18.5:
    print("Your BMI is %.2f and you are underweight!" % bmi)
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI is %.2f and you are of normal weight :)" % bmi)
elif bmi >= 25.0 and bmi <= 29.9:
    print("Your BMI is %.2f and you are overweight!" % bmi)
else:
    print("Your BMI is %.2f and you are obese!" % bmi)
