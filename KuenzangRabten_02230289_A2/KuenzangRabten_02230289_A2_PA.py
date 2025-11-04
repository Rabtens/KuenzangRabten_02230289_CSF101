"""
Part A - Searching Algorithms
File: KuenzangRabten_02230289_A2_PA.py
Author: Kuenzang Rabten (02230289)
Simple menu program: Linear Search and Binary Search
"""

def linear_search(arr, target):
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return i + 1, comparisons  # 1-indexed position
    return -1, comparisons


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid + 1, comparisons  # 1-indexed
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


def part_a_menu():
    # Hardcoded lists (20 items each)
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007,
                   1012, 1015, 1011, 1006, 1013, 1014, 1020, 1021, 1016,
                   1017, 1018]

    sorted_scores = [35, 42, 46, 51, 55, 58, 62, 66, 69, 72,
                     75, 78, 81, 84, 88, 90, 92, 95, 97, 100]

    print("=== Searching Algorithms Menu ===")
    while True:
        print("\nSelect a search operation (1-3):")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            print("\nSearching in the list:", student_ids)
            try:
                target = int(input("Enter Student ID to search: ").strip())
            except ValueError:
                print("Please enter a valid integer Student ID.")
                continue
            pos, comps = linear_search(student_ids, target)
            if pos != -1:
                print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comps}")
            else:
                print(f"Result: Student ID {target} not found Comparisons made: {comps}")

        elif choice == '2':
            print("\nSorted scores:", sorted_scores)
            try:
                target = int(input("Enter score to search: ").strip())
            except ValueError:
                print("Please enter a valid integer score.")
                continue
            pos, comps = binary_search(sorted_scores, target)
            if pos != -1:
                print(f"Result: Score {target} found at position {pos} Comparisons made: {comps}")
            else:
                print(f"Result: Score {target} not found Comparisons made: {comps}")

        elif choice == '3':
            print("\nSearch program laglen thab nang mi lu kadrinchay!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            continue

        again = input("Would you like to perform another search? (y/n): ").strip().lower()
        if again != 'y':
            print("\nSearch program laglen thab nang mi lu kadrinchay!")
            break


if __name__ == '__main__':
    part_a_menu()