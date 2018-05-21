# Ask for the names to greet
names_str = input("Who would you like to greet? ")

# Convert the name to list
names = names_str.split(",")

# Greet each person
for index, name in enumerate(names):
    #Remove spaces from the start and end of the name
    name = name.strip()
    message = "Hello " + name + ". You are the " + str(index + 1)
    if (index + 1) % 10 == 1:
        message += "st"
    elif (index + 1) % 10 == 2:
        message += "nd"
    elif (index + 1) % 10 == 3:
        message += "rd"
    else:
        message += "th"
    message += " Person."

    print(message)

