import random

def guess_the_number():
    print("🎲 Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("🔼 Too low! Try again.")
        elif guess > number:
            print("🔽 Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break
    else:
        print(f"😢 Sorry, you're out of attempts. The number was {number}.")

if __name__ == "__main__":
    guess_the_number()
