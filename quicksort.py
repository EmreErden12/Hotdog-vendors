hotdog_data = []

# Load data from file
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Remove newline and split by comma
            items = line.strip().split(',')

            # Validation: correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found")
    hotdog_data = []


# Quick sort function
def quick_sort(data):

    # Validation: empty or single item list
    if len(data) <= 1:
        return data

    # Choose pivot (middle value based on vendor name)
    pivot = data[len(data) // 2][1].lower()

    left = []
    middle = []
    right = []

    for row in data:

        # Safety check
        if len(row) < 2:
            continue

        value = row[1].lower()

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

    print("\nOrganised Data Set (Sorted by Brand)\n")

    for row in sorted_data:
        print(row)

else:
    print("No data to sort.")



