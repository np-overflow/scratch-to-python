# Ask for width of the pyramid
radius_str = input("What is the radius of the base of the pyramid? ")

# Convert the width from string to int
radius = int(radius_str)

# Draw the pyramid
for i in range(1, radius+1):
    message = " " * (radius -i)
    message += "*" * (i*2)
    message += " " * (radius -i)
    print(message)

