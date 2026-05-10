# Load data from file
hotdog_data = []

try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Split line into list values
            items = line.strip().split(',')

            # Validate correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found")
    hotdog_data = []


# Sort data by vendor name before binary search
hotdog_data = sorted(hotdog_data, key=lambda row: row[1].lower())


# Binary search function
def binary_search_brand(data, search_term):

    # Check if data exists
    if len(data) == 0:
        print("No data available")
        return None

    # Validate input
    search_term = search_term.strip().lower()

    if search_term == "":
        print("Error: search term cannot be empty")
        return None

    # Set search range
    low = 0
    high = len(data) - 1

    # Binary search loop
    while low <= high:

        mid = (low + high) // 2
        current_value = data[mid][1].lower()

        if current_value == search_term:
            return data[mid]

        elif current_value < search_term:
            low = mid + 1

        else:
            high = mid - 1

    return None


# User input
search_term = input("Enter a vendor name to search: ")

# Run search
result = binary_search_brand(hotdog_data, search_term)

# Output result
if result:
    print("\nMatch found:", result)
else:
    print("\nVendor not found")

