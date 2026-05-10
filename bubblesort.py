hotdog_data = []

# Load data from file
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Clean and split line
            items = line.strip().split(',')

            # Validation: check correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found")
    hotdog_data = []


# Bubble sort function (sorting by vendor name)
def bubble_sort_by_brand(data):

    # Check if data exists
    if len(data) == 0:
        print("No data to sort")
        return data

    # Get length of dataset
    n = len(data)

    # Bubble sort process
    # Repeatedly compare adjacent values and swap if needed
    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare vendor names (column 1)
            if data[j][1].lower() > data[j + 1][1].lower():

                # Swap values
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    return data


# Run bubble sort
sorted_data = bubble_sort_by_brand(hotdog_data)

# Output results
print("\nOrganised Data Set (Sorted by Brand)\n")

for row in sorted_data:
    print(row)
