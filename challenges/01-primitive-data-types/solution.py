height = input('What is your height (cm)? ')
height = int(height) / 100

weight = input('What is your weight (kg)? ')
weight = int(weight)

bmi = weight / (height * height)
bmi = str(bmi)
print('Your BMI is ' + bmi + '!')
