# Challenge 4: Loops and Lists
In this challenge, you have been tasked to write a program that prints a message for each person in the list. 

# Challenge 4.1: Simple loops
### Inputs
- The  `lists` of the people to greet

### Outputs
- `"Hello {name}. You are No. {no} in the list."`

### Tips
- Use enumerate to get the index of the list

### Sample
```
Who would you like to greet? Bob, Mary, Jane, Judy

Hello Bob. You are No. 1 in the list. 
Hello Mary. You are No. 2 in the list. 
Hello Jane. You are No. 3 in the list. 
Hello Judy. You are No. 4 in the list. 
```

# Challenge 4.2: FizzBuzz!

Iterate through and print the numbers from 1 to 100. If a number is divisible by 3, print `Fizz`. If it is divisible by 5, print `Buzz`. If it is divisible by both 3 and 5, print `FizzBuzz`

### Inputs
- A `list` containing the numbers 1 - 100.

### Outputs
- `{number}/Fizz/Buzz/FizzBuzz`

### Tips
- Use the `%` operator to find if a number is divisible by an integer of your own choosing

### Sample
```
1
2
Fizz
3
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```