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
            print(" Invalid choice. Try again.")

def give_hint(guess, number):
    difference = abs(guess - number)

    if difference == 0:
        return " Exact match!"

    if difference <= 3:
        return "🔥 Very Hot!"
    elif difference <= 7:
        return "🌡 Warm"
    else:
        return "❄ Cold"

def play():
    start, end, attempts = choose_level()
    number = random.randint(start, end)

    print(f"\nI'm thinking of a number between {start} and {end}.")
    print(f"You have {attempts} attempts. Good luck!\n")

    while attempts > 0:
        guess = input("Your guess: ").strip()

        if not guess.isdigit():
            print(" Please enter a valid integer.\n")
            continue

        guess = int(guess)
        attempts -= 1

        if guess == number:
            print(f" Correct! The number was {number}.")
            break
        else:
            print(give_hint(guess, number))

            if guess < number:
                print("   ➤ Hint: Go Higher!")
            else:
                print("   ➤ Hint: Go Lower!")

        print(f"Attempts left: {attempts}\n")

    if attempts == 0:
        print(f"\n You're out of attempts! The correct number was {number}.")

def main():
    while True:
        play()
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n Thanks for playing!")
            break

if _name_ == "_main_":
    main()
