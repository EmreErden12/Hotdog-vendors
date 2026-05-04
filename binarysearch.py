hotdog_data = []

# Load data
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Split each line into list values
            items = line.strip().split(',')

            # Check row has correct number of values
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: file not found")


# Binary search function
def binary_search_brand(data, search_term):

    # 1. Check if data exists
    if len(data) == 0:
        print("No data available")
        return

    # 2. Validate search input
    if search_term is None or search_term.strip() == "":
        print("Error: search term cannot be empty")
        return

    search_term = search_term.strip().lower()

    # 3. Sort data by brand (important for binary search)
    data.sort()

    # 4. Set up binary search values
    low = 0
    high = len(data) - 1
    found = False

    # 5. Binary search loop
    while low <= high:

        mid = (low + high) // 2
        current_value = data[mid][1].lower()

        # Check if match found
        if current_value == search_term:
            print("Found:", data[mid])
            found = True
            break

        # Move search range
        elif current_value < search_term:
            low = mid + 1
        else:
            high = mid - 1

    # 6. If not found
    if not found:
        print("Brand not found")


# Run search
search = input("Enter brand to search: ")
binary_search_brand(hotdog_data, search)


