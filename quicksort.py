# Quick Sort function (sorts by column index 1 = Brand)
def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2][1]

    left = []
    middle = []
    right = []

    for row in data:
        if row[1] < pivot:
            left.append(row)
        elif row[1] > pivot:
            right.append(row)
        else:
            middle.append(row)

    return quick_sort(left) + middle + quick_sort(right)


# Apply Quick Sort
hotdog_data = quick_sort(hotdog_data)

# Print sorted data
print("Organised Data Set (Sorted by Brand using Quick Sort)")
for row in hotdog_data:
    print(row)
