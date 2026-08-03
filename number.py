import random

best_score = None


def choose_difficulty():
    print("\nChoose Difficulty Level")
    print("1. Easy   (10 Attempts)")
    print("2. Medium (7 Attempts)")
    print("3. Hard   (5 Attempts)")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def play_game():
    global best_score

    secret_number = random.randint(1, 100)
    max_attempts = choose_difficulty()
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            score = (max_attempts - attempts + 1) * 10

            print("\nCongratulations!")
            print("You guessed the correct number.")
            print("Attempts Used :", attempts)
            print("Score         :", score)

            if best_score is None or score > best_score:
                best_score = score
                print("New Best Score!")

            return

        elif guess < secret_number:
            print("Too Low.")

            if secret_number - guess <= 10:
                print("Hint: You are very close.")

        else:
            print("Too High.")

            if guess - secret_number <= 10:
                print("Hint: You are very close.")

        print("Attempts Left:", max_attempts - attempts)

    print("\nGame Over!")
    print("The correct number was:", secret_number)


def main():

    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)

    while True:

        play_game()

        if best_score is not None:
            print("\nBest Score:", best_score)

        choice = input("\nDo you want to play again? (yes/no): ").lower()

        if choice != "yes":
            print("\nThank you for playing.")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()