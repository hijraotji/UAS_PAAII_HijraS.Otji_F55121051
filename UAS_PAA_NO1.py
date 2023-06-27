import time

def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # Tampilkan 5 iterasi pertama
        if i < 5:
            print(f"Iteration {i + 1}: {arr}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Tampilkan 5 iterasi terakhir
    print(f"\nFinal Iteration: {arr}")
    print(f"Elapsed Time: {elapsed_time} seconds")
    print("--------------------------------------")


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        # Tampilkan 5 iterasi pertama
        if i < 5:
            print(f"Iteration {i}: {arr}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Tampilkan 5 iterasi terakhir
    print(f"\nFinal Iteration: {arr}")
    print(f"Elapsed Time: {elapsed_time} seconds")
    print("--------------------------------------")


# List yang diberikan
arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33, 90, 90, 7,
       26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84, 32, 5, 3, 44, 21, 10, 21,
       17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6, 3, 1, 40, 22, 43, 18, 1, 77, 9, 59,
       40, 7, 41, 81]

print("Before sorting:", arr)
print("--------------------------------------")

choice = input("Choose sorting algorithm (bubble/insertion): ")

if choice == "bubble":
    bubble_sort(arr.copy())
elif choice == "insertion":
    insertion_sort(arr.copy())
else:
    print("Invalid choice.")

print("After sorting:", arr)
