# Ask for height
height = input('What is your height (cm)? ')

# Convert height from string to integer and convert from cm to m
height = int(height) / 100

# Ask for weight
weight = input('What is your weight (kg)? ')

# Convert height from string to integer
weight = int(weight)

# Calculate BMI
bmi = weight / (height * height)

# Print out the BMI
print('Your BMI is %.2f!' % bmi)
