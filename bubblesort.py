n = len(hotdog_data)
for i in range(n):
    for j in range(0, n - i - 1):
        # We look at [1] because 'Dolly Dogs', 'Vegan Dogs' etc. are the second items
        if hotdog_data[j][1] > hotdog_data[j + 1][1]:
            # Swap the entire rows
            temp = hotdog_data[j]
            hotdog_data[j] = hotdog_data[j + 1]
            hotdog_data[j + 1] = temp

# 3. Print the organized data set
print("Organised Data Set (Sorted by Brand)")
for row in hotdog_data:
    print(row)

