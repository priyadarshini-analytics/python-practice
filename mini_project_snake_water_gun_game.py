import random


def game_win(user, computer):
    if user == computer:
        return None

    winning_matches = {
        ("snake", "water"),
        ("water", "gun"),
        ("gun", "snake"),
    }
    return (user, computer) in winning_matches


def main():
    choices = ["snake", "water", "gun"]

    print("Welcome to the Snake Water Gun Game!")
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (snake/water/gun): ").strip().lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose snake, water, or gun.")
        return

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    result = game_win(user_choice, computer_choice)
    if result is None:
        print("It's a tie!")
    elif result:
        print("You win!")
    else:
        print("Computer wins!")


if __name__ == "__main__":
    main()

























































