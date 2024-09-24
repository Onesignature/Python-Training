import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("------Welcome to the guessing game-------")
print(f"Select a number between {lowest_num} to {highest_num}")

while is_running:
    guess = int(input("Enter your guess: "))
    if guess < lowest_num or guess > highest_num:
        print("That number is out of range.")
        print(f"Select a number between {lowest_num} to {highest_num}")
    elif guess < answer:
        print("Too low, try again!")
        guesses += 1
    elif guess > answer:
        print("Too high, try again!")
        guesses += 1
    else:
        print("That is the correct answer!")
        print(f"Number of guess: {guesses}")
        is_running = False
