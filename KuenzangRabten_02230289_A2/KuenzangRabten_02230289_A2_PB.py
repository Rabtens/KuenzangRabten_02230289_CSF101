"""
Part B - Sorting Algorithms
File: KuenzangRabten_02230289_A2_PB.py
Author: Kuenzang Rabten (02230289)
Menu program: Bubble Sort, Insertion Sort, Quick Sort
"""

from typing import List, Tuple


def bubble_sort_names(names: List[str]) -> Tuple[List[str], int]:
    arr = names[:]
    n = len(arr)
    swaps = 0
    # Simple bubble sort (alphabetical)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return arr, swaps


def insertion_sort_scores(scores: List[int]) -> List[int]:
    arr = scores[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def quick_sort_prices(arr: List[int], counter: dict) -> List[int]:
    # counter is a dict used to count recursive calls
    counter['calls'] += 1
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_prices(left, counter) + middle + quick_sort_prices(right, counter)


def part_b_menu():
    # Hardcoded lists
    student_names = [
        "Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Tandin", "Chimmi",
        "Dorji", "Pema", "Sangay", "Kinzang", "Tashi", "Yonten", "DorjiW",
        "Kezang"
    ]  # 15 names

    test_scores_unsorted = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
                             76, 85, 48, 93, 71, 89, 57, 80, 69, 60]

    book_prices = [450, 230, 678, 125, 890, 299, 150, 999, 499, 320, 210, 410, 375, 540, 275]

    print("=== Sorting Algorithms Menu ===")
    while True:
        print("\nSelect a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            print("\nOriginal:", student_names)
            sorted_names, swaps = bubble_sort_names(student_names)
            print("Sorted:", sorted_names)
            print(f"Total swaps made: {swaps}")

        elif choice == '2':
            print("\nOriginal scores:", test_scores_unsorted)
            sorted_scores = insertion_sort_scores(test_scores_unsorted)
            print("Performing Insertion Sort...")
            print("Sorted scores:", sorted_scores)
            # Top 5 scores (highest first)
            top5 = sorted(sorted_scores, reverse=True)[:5]
            print("Top 5 Scores:")
            for i, s in enumerate(top5, 1):
                print(f"{i}. {s}")

        elif choice == '3':
            print("\nOriginal prices:", book_prices)
            counter = {'calls': 0}
            sorted_prices = quick_sort_prices(book_prices, counter)
            print("Sorted prices:", sorted_prices)
            print(f"Recursive calls: {counter['calls']}")

        elif choice == '4':
            print("\nThank you for using the sorting program!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")
            continue

        again = input("Would you like to perform another sort? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using the sorting program!")
            break


if __name__ == '__main__':
    part_b_menu()