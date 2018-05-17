# Ask for user input first
height_str = input("What is your height (cm)? ")
weight_str = input("What is your weight (kg)? ")

#Convert user input string to floats
height = float(height_str)
weight = float(weight_str)

#Convert height in cm to height in meters
height = height / 100

#Calculate BMI
bmi = weight / (height * height)

#Check the BMI status
if bmi < 18.5:
    print("Your BMI is %.2f and you are underweight" % bmi)
elif bmi >=18.5 and bmi <= 24.9:
    print("Your BMI is %.2f and you are of normal weight :)" % bmi)
elif bmi >=25.0 and bmi <= 29.9:
    print("Your BMI is %.2f and you are overweight" % bmi)
elif bmi > 30.0:
    print("Your BMI is %.2f and you are obese" % bmi)
