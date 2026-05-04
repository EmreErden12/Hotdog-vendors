# 1. ask the user for what they want to find
search_term = input("Enter the name or value to search for: ")

found = False

# 2. iterate through each row in the 2D list
for row in hotdog_data:
    # 3. check if the search term exists in this specific row
    if search_term in row:
        print(f"Match found: {row}")
        found = True
        break  # stop searching once we find a match

if not found:
    print("Item not found in the file.")
