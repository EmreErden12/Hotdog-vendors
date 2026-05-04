hotdog_data = []

# Load data
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # 1. Split line into list
            items = line.strip().split(',')

            # 2. Validate row has correct number of columns
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: file not found")


# Binary search
def binary_search_brand(data, search_term):

    # 1. Check if data exists
    if not data:
        print("Error: no data loaded")
        return

    # 2. Validate search input
    if search_term is None:
        print("Error: no search term provided")
        return

    search_term = search_term.strip()

    if search_term == "":
        print("Error: search term cannot be empty")
        return

    search_term = search_term.lower()

    # 3. Sort data by brand (needed for binary search)
    data.sort()

    # 4. Set up binary search variables
    low = 0
    high = len(data) - 1
    found = False

    # 5. Binary search loop
    while low <= high:

        mid = (low + high) // 2
        current_value = data[mid][1].lower()

        # 6. Check for match
        if current_value == search_term:
            print("Found:", data[mid])
            found = True
            break

        # 7. Move search range
        elif current_value < search_term:
            low = mid + 1
        else:
            high = mid - 1

    # 8. If not found
    if not found:
        print("Brand not found")


# Run search
search = input("Enter brand to search: ")
binary_search_brand(hotdog_data, search)


