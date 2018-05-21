# Ask for width of the triangle
width_str = input("What is the base of the pyramid? ")

# Convert the width from string to int
width = int(width_str)

# Draw the pyramid
for i in range(1, width+1):
    message = "*" * i
    print(message)

