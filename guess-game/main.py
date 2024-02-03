import random
from art import logo

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is 13\n""")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

guesed_number = random.randint(1, 100)

i = 0

while i <= attempts - 1:
    print(f"You have {attempts - i} attempts remaining to guess the number.")
    make_a_guess = int(input("Make a guess: "))
    if make_a_guess < guesed_number:
        print("Too law.")
    elif make_a_guess > guesed_number:
        print("Too high.")
    else:
        print("You win.")
        break
    i = i + 1
    if i == attempts:
        print("You lose.")