import random
import timeit

# Insertion Sort implementation
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Define array sizes
sizes = [100, 1000, 5000]

print("\nPerformance Comparison of Sorting Algorithms\n")

for size in sizes:
    print(f"Testing array of size {size}...")
    
    # Generate a random array of integers
    data = [random.randint(0, 10000) for _ in range(size)]

    # Create separate copies for each sorting algorithm
    insertion_data = data.copy()
    merge_data = data.copy()
    timsort_data = data.copy()

    # Measure execution time of Insertion Sort (in-place)
    insertion_time = timeit.timeit(lambda: insertion_sort(insertion_data.copy()), number=1)

    # Measure execution time of Merge Sort (returns new list)
    merge_time = timeit.timeit(lambda: merge_sort(merge_data.copy()), number=1)

    # Measure execution time of built-in sorted() function (uses Timsort)
    timsort_time = timeit.timeit(lambda: sorted(timsort_data.copy()), number=1)

    # Print timing results
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Merge Sort Time:     {merge_time:.6f} seconds")
    print(f"Timsort Time:        {timsort_time:.6f} seconds")
    print("-" * 40)

