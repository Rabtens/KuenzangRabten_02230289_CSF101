"""
Author: Kuenzang Rabten
Student Number: 02230289
Assignment 1 - Part A
Description: A command-line Python program with six functions:
1. Perfect number sum
2. Weight converter
3. Vowel counter
4. Average and range finder
5. String reverser with word count
6. Specific word counter (from text file)
"""

import urllib.request

def is_perfect(num):
    "Check if a number is perfect."
    if num < 2:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num


def perfect_number_sum():
    "Find and display the sum of perfect numbers in a given range."
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))
        if start > end or start < 1:
            print("Invalid range. Try again.")
            return
        total = sum(num for num in range(start, end + 1) if is_perfect(num))
        print(f"Sum of perfect numbers between {start} and {end} is: {total}")
    except ValueError:
        print("Please enter valid integers.")


def weight_converter():
    "Convert weight between kilograms and pounds."
    try:
        value = float(input("Enter weight value: "))
        unit = input("Convert to (K for kilograms, P for pounds): ").strip().upper()
        if unit == 'K':
            converted = value / 2.205
            print(f"{value} pounds = {round(converted, 2)} kilograms")
        elif unit == 'P':
            converted = value * 2.205
            print(f"{value} kilograms = {round(converted, 2)} pounds")
        else:
            print("Invalid conversion type. Use 'K' or 'P'.")
    except ValueError:
        print("Please enter a valid number.")


def vowel_counter():
    "Count vowels in a string."
    text = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print(f"Number of vowels: {count}")


def average_and_range():
    "Find average and range of a series of numbers."
    try:
        n = int(input("How many numbers do you want to enter? "))
        if n <= 0:
            print("Number of entries must be greater than zero.")
            return
        numbers = []
        for i in range(n):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
        avg = sum(numbers) / len(numbers)
        num_range = max(numbers) - min(numbers)
        print(f"Average: {round(avg, 2)}, Range: {round(num_range, 2)}")
    except ValueError:
        print("Please enter valid numbers.")


def string_reverser():
    "Reverse a string and count the number of words."
    text = input("Enter a string: ").strip()
    reversed_text = text[::-1]
    word_count = len([word for word in text.split() if word])
    print(f"Reversed String: {reversed_text}")
    print(f"Word count: {word_count}")


def specific_word_counter():
    "Count specific words ['kuzu', 'laso', 'tashi', 'yangchen'] in a text file."
    words_to_count = ["kuzu", "laso", "tashi", "yangchen"]
    counts = {word: 0 for word in words_to_count}

    try:
        # Used a sample text file from a URL for demonstration since it was not manually saved.
        url = "https://gist.githubusercontent.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c/raw/"
        response = urllib.request.urlopen(url)
        text = response.read().decode('utf-8').lower()

        for word in words_to_count:
            counts[word] = text.split().count(word)

        for word, count in counts.items():
            print(f"'{word}': {count}")
    except Exception as e:
        print("Error reading file:", e)


def main():
    "Main program loop."
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate sum of perfect numbers")
        print("2. Convert weight units")
        print("3. Count vowels in string")
        print("4. Find average and range of numbers")
        print("5. Reverse string and count words")
        print("6. Count specific words in text file")
        print("0. Exit program")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            perfect_number_sum()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            vowel_counter()
        elif choice == '4':
            average_and_range()
        elif choice == '5':
            string_reverser()
        elif choice == '6':
            specific_word_counter()
        elif choice == '0':
            print("Exiting program. Tashi Delek")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

        again = input("\nWould you like to try another function? (y/n): ").strip().lower()
        if again != 'y':
            print("Ani Program use bay nang mi lu kadrinchay")
            break


if __name__ == "__main__":
    main()