import time

# Test cases (multiple searches)
test_cases = ["Dolly Dogs", "Korner Kart", "Emre Dogs"]

runs = 10000

print("\n--- SEARCH EFFICIENCY TEST ---")


# Loop through each test case
for search_term in test_cases:

    print("\nTesting:", search_term)


    # Linear search timing
    start_time = time.perf_counter()

    for i in range(runs):
        linear_search_by_id(hotdog_data, search_term)

    end_time = time.perf_counter()

    linear_time = (end_time - start_time) / runs


    # Binary search timing
    start_time = time.perf_counter()

    for i in range(runs):
        binary_search_brand(hotdog_data, search_term)

    end_time = time.perf_counter()

    binary_time = (end_time - start_time) / runs


    # Output results
    print("Linear Search Time:", linear_time)
    print("Binary Search Time:", binary_time)
