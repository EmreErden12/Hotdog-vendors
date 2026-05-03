# 1. load the data and swap columns so Brand is first
with open('Hotdog.txt', 'r') as file:
    for line in file:
        items = line.strip().split(',')
        if len(items) > 1:
            # putting items[1] (Brand) at the front of a new list
            # format: [Brand, ID, Date, Calories...]
            cleaned_row = [items[1], items[0], items[2], items[3], items[4]]
            hotdog_data.append(cleaned_row)

hotdog_data.sort()

# 3. setup variables
search_term = input("Enter a brand to search for: ")
low = 0
high = len(hotdog_data) - 1
result = None

# 4. standard Binary Search
while low <= high:
    mid = (low + high) // 2
    
    # since Brand is now at [0], this comparison works
    if hotdog_data[mid][0] == search_term:
        result = hotdog_data[mid]
        break 
    elif hotdog_data[mid][0] < search_term:
        low = mid + 1
    else:
        high = mid - 1

# 5. output
if result:
    print(f"Found: {result}")
else:
    print("Brand not found.")
