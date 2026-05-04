hotdog_data = []
with open('Hotdog.txt', 'r') as file:
    for line in file:
          # 1. .strip() removes the newline character
          # 2. .split(',') breaks the string into a list based on commas
          items = line.strip().split(',')

          # Add the resulting list to our main list
          hotdog_data.append(items)

# Test example: print all data to check it is in the list
for i in (hotdog_data):
    print(i)

# Example: Accessing the first item of the first row
print(hotdog_data[0])






