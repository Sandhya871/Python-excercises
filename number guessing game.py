import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True

print("Python number guessing game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter a guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num} ")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! the answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else: 
        print("Invalid guess")
        print(f"Please Select a number between {lowest_num} and {highest_num} ")


''' Randomly generates a number and allows the user to guess until the correct number is found. '''

# OUTPUT
Python number guessing game
Select a number between 1 and 100
Enter a guess: 50
Too high! Try again!
Enter a guess: 30
Too high! Try again!
Enter a guess: 24
Too low! Try again!
Enter a guess: 25
CORRECT! the answer was 25
Number of guesses: 4
