import time
import copy

#  Number of runs for average timing 
runs = 100

print("\n--- SORT EFFICIENCY TEST ---")


# 1. Bubble sort timing

start_time = time.perf_counter()

for i in range(runs):

    # Copy data so each run starts fresh
    temp_data = copy.deepcopy(hotdog_data)

    bubble_sort_by_brand(temp_data)

end_time = time.perf_counter()

bubble_time = (end_time - start_time) / runs


# 2. Quick sort timing

start_time = time.perf_counter()

for i in range(runs):

    # Copy data so each run starts fresh
    temp_data = copy.deepcopy(hotdog_data)

    quick_sort(temp_data)

end_time = time.perf_counter()

quick_time = (end_time - start_time) / runs


# 3. RESULTS OUTPUT

print("\nSORTING EFFICIENCY RESULTS")
print("Bubble Sort Time:", bubble_time)
print("Quick Sort Time:", quick_time)
