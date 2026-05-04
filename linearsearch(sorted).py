hotdog_data = []

# Load data
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Split line into lis of values
            items = line.strip().split(',')

            # Basic validation: ensure correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found.")
    hotdog_data = []


# Libear search function
def search_any(data, search_term=None):
    """
    Linear search through an unsorted list.
    Checks all fields in each row.
    Returns first match or None.
    """

    # Ask user if no search term provided
    if search_term is None:
        search_term = input("Enter value to search for: ")

    # Validation
    search_term = search_term.strip()

    if search_term == "":
        print("Error: search term cannot be empty.")
        return None

    search_term = search_term.lower()

    # Search process
    for row in data:

        for item in row:

            # Safe comparison (handles numbers + strings)
            if search_term in str(item).lower():
                return row

    # If nothing found
    print("No matching result found.")
    return None


# Run search
result = search_any(hotdog_data)

print("\nSEARCH RESULT")
print(result)
