# Ask for the names to greet
names_str = input("Who would you like to greet? ")

# Convert the name to list
names = names_str.split(",")

# Greet each person
for index, name in enumerate(names):
    #Remove spaces from the start and end of the name
    name = name.strip()
    message = "Hello " + name + ". You are No. " + str(index + 1) + "in the list."
    print(message)

