# guess_game_levels.py
import random

def choose_level():
    print("\nChoose difficulty level:")
    print("1. Easy   (Range: 1–10   | Attempts: 5)")
    print("2. Medium (Range: 1–50   | Attempts: 7)")
    print("3. Hard   (Range: 1–100  | Attempts: 10)")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return 1, 10, 5
        elif choice == "2":
            return 1, 50, 7
        elif choice == "3":
            return 1, 100, 10
        else:
            print("Invalid choice. Try again.")

def play():
    start, end, attempts = choose_level()
    number = random.randint(start, end)

    print(f"\nI'm thinking of a number between {start} and {end}.")
    print(f"You have {attempts} attempts. Good luck!\n")

    while attempts > 0:
        guess = input("Your guess: ").strip()

        if not guess.isdigit():
            print("❌ Please enter a valid integer.\n")
            continue

        guess = int(guess)
        attempts -= 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"✅ Correct! The number was {number}.")
            break

        print(f"Attempts left: {attempts}\n")

    if attempts == 0:
        print(f"\n❌ Out of attempts! The correct number was {number}.")

if __name__ == "__main__":
    play()