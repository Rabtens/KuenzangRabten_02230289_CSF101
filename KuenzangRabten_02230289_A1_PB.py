"""
Author: Kuenzang Rabten
Student Number: 02230289
Assignment 1 - Part B
Description: Two simple games:
1. Guess Number Game
2. Rock Paper Scissors Game
"""

import random

def guess_number_game():
    "Play a number guessing game (1–100)."
    number = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100...")

    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Tiktik Phobchi! The number was {number}. Attempts: {attempts}")
                break
        except ValueError:
            print("Please enter a valid number.")


def rock_paper_scissors():
    "Play Rock Paper Scissors against the computer."
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0

    while True:
        print("\nEnter your choice (rock/paper/scissors) or 'q' to quit:")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == 'q':
            print(f"Final Score → You: {user_wins}, Computer: {computer_wins}")
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("Zai choe gay sui!")
            user_wins += 1
        else:
            print("Computer Gaysi ro!")
            computer_wins += 1


def main():
    "Main game menu."
    while True:
        print("\nSelect a game (1-3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit program")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Exiting the game program. Tashi Delek!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()  