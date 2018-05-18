# Ask for width of the pyramid
width_str = input("What is the radius of the base of the pyramid? ")

# Convert the width from string to int
width = int(radius_str)

# hWidth is half the width of the pyramid
hWidth = width // 2 


# Draw the pyramid
for i in range(1, hWidth+1):
    message = " " * (radius -i)
    message += "*" * (i*2)
    message += " " * (radius -i)
    print(message)

