
hotdog_data = []

# Load data from file
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # 1. remove newline and split by comma
            items = line.strip().split(',')

            # validation: correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found.")
    hotdog_data = []

# Test: print data to check it loaded correctly
for i in hotdog_data:
    print(i)

# Example: access first row safely
if len(hotdog_data) > 0:
    print(hotdog_data[0])
else:
    print("No data loaded.")

# Quick Sort Function
def quick_sort(data):

    # validation: empty or single item list
    if len(data) <= 1:
        return data

    # choose pivot (middle value)
    pivot = data[len(data) // 2][1]

    left = []
    middle = []
    right = []

    for row in data:

        # safety check
        if len(row) < 2:
            continue

        value = row[1]

        if value < pivot:
            left.append(row)

        elif value == pivot:
            middle.append(row)

        else:
            right.append(row)

    return quick_sort(left) + middle + quick_sort(right)

# Run sort
if len(hotdog_data) > 0:

    sorted_data = quick_sort(hotdog_data)

    print("\n--- SORTED DATA (Quick Sort) ---")
    for row in sorted_data:
        print(row)

else:
    print("No data to sort.")


