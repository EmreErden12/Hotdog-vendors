hotdog_data = []

# Load data
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # 1. Clean and split line
            items = line.strip().split(',')

            # 2. Validation: check correct number of columns
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found")


# TEST PRINT (original data)
print("--- Original Data ---")
for row in hotdog_data:
    print(row)

# Example check (only if data exists)
if hotdog_data:
    print("\nFirst row:", hotdog_data[0])


# BUBBLE SORT FUNCTION
def bubble_sort_by_brand(data):

    # 1. Check if data exists
    if len(data) == 0:
        print("No data to sort")
        return

    # 2. Get length of list
    n = len(data)

    # 3. Bubble sort loop
    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare brand names (column 1)
            if data[j][1].lower() > data[j + 1][1].lower():

                # swap rows
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp

    # 4. Print sorted data
    print("\nOrganised Data Set (Sorted by Brand)-")

    for row in data:
        print(row)


# RUN SORT
bubble_sort_by_brand(hotdog_data)

