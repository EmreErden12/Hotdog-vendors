hotdog_data = []

# Load data from file
try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            # Remove newline character and split by comma
            items = line.strip().split(',')

            # Validation: check correct number of fields
            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found.")
    hotdog_data = []

# Test: print all data to check it is loaded correctly
for i in hotdog_data:
    print(i)

# Example: access first row
if len(hotdog_data) > 0:
    print(hotdog_data[0])
else:
    print("No data loaded.")

# Linear Search with validation

search_term = input("Enter the name or value to search for: ")

# Validation: remove spaces
search_term = search_term.strip()

if search_term == "":
    print("Error: search term cannot be empty.")
else:

    found = False

    # search through dataset
    for row in hotdog_data:

        if search_term in row:

            print("Match found:", row)
            found = True
            break

    if not found:
        print("Item not found in the file.")
