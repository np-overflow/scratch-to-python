# Ask for height
height = input('What is your height (cm)? ')
height = int(height) / 100 # Convert to m

# Ask for weight
weight = input('What is your weight (kg)? ')
weight = int(weight)

# Calculate BMI
bmi = weight / (height * height)

# Print out the BMI
print('Your BMI is %.2f!' % bmi)
