# Load data from file
hotdog_data = []

try:
    with open('Hotdog.txt', 'r') as file:
        for line in file:

            items = line.strip().split(',')

            if len(items) == 7:
                hotdog_data.append(items)
            else:
                print("Skipping invalid row:", items)

except FileNotFoundError:
    print("Error: Hotdog.txt file not found")
    hotdog_data = []


# Analyse data function
def analyse_data(data):

    if len(data) == 0:
        print("No data available to analyse.")
        return None

    vendors = {}

    for row in data:

        try:
            vendor = row[1]
            vegan = int(row[3])
            meat = int(row[4])
            onions = float(row[5])
            ketchup = float(row[6])

        except ValueError:
            print("Skipping invalid row:", row)
            continue

        total = vegan + meat

        if vendor not in vendors:
            vendors[vendor] = {
                "vegan": 0,
                "meat": 0,
                "total": 0,
                "onions": 0,
                "ketchup": 0
            }

        vendors[vendor]["vegan"] += vegan
        vendors[vendor]["meat"] += meat
        vendors[vendor]["total"] += total
        vendors[vendor]["onions"] += onions
        vendors[vendor]["ketchup"] += ketchup

    # Most productive vendor
    most_productive = ""
    highest_total = -1

    for vendor in vendors:
        if vendors[vendor]["total"] > highest_total:
            highest_total = vendors[vendor]["total"]
            most_productive = vendor

    # Totals
    total_vegan = 0
    total_meat = 0

    for vendor in vendors:
        total_vegan += vendors[vendor]["vegan"]
        total_meat += vendors[vendor]["meat"]

    # Ketchup usage
    least_ketchup_vendor = ""
    most_ketchup_vendor = ""
    least_ketchup = float("inf")
    most_ketchup = -1

    for vendor in vendors:

        ketchup_total = vendors[vendor]["ketchup"]

        if ketchup_total < least_ketchup:
            least_ketchup = ketchup_total
            least_ketchup_vendor = vendor

        if ketchup_total > most_ketchup:
            most_ketchup = ketchup_total
            most_ketchup_vendor = vendor

    # Onion usage
    most_onions_vendor = ""
    most_onions = -1

    for vendor in vendors:

        if vendors[vendor]["onions"] > most_onions:
            most_onions = vendors[vendor]["onions"]
            most_onions_vendor = vendor

    # Efficiency
    most_efficient_vendor = ""
    least_efficient_vendor = ""
    best_ratio = float("inf")
    worst_ratio = -1

    for vendor in vendors:

        if vendors[vendor]["total"] == 0:
            continue

        ratio = vendors[vendor]["ketchup"] / vendors[vendor]["total"]

        if ratio < best_ratio:
            best_ratio = ratio
            most_efficient_vendor = vendor

        if ratio > worst_ratio:
            worst_ratio = ratio
            least_efficient_vendor = vendor

    return (most_productive, total_vegan, total_meat,
            least_ketchup_vendor, most_ketchup_vendor,
            most_onions_vendor, most_efficient_vendor,
            least_efficient_vendor)


# Save results function
def save_results(filename, results):

    try:
        with open(filename, 'w') as file:

            file.write("Hotdog Analysis Report\n")
            file.write("======================\n\n")

            file.write("Most Productive Vendor: " + str(results[0]) + "\n\n")

            file.write("Total Vegan Sales: " + str(results[1]) + "\n")
            file.write("Total Meat Sales: " + str(results[2]) + "\n\n")

            file.write("Least Ketchup Vendor: " + str(results[3]) + "\n")
            file.write("Most Ketchup Vendor: " + str(results[4]) + "\n\n")

            file.write("Most Onions Vendor: " + str(results[5]) + "\n\n")

            file.write("Most Efficient Vendor: " + str(results[6]) + "\n")
            file.write("Least Efficient Vendor: " + str(results[7]) + "\n")

    except Exception as e:
        print("Error saving results:", e)


# Linear search (checks all fields)
def linear_search(data, search_term):

    search_term = search_term.strip().lower()

    if search_term == "":
        return None

    for row in data:
        for item in row:

            if search_term in str(item).lower():
                return row

    return None


# Binary search (sorted by vendor name)
def binary_search(data, search_term):

    if len(data) == 0:
        return None

    search_term = search_term.strip().lower()

    if search_term == "":
        return None

    sorted_data = sorted(data, key=lambda row: row[1].lower())

    low = 0
    high = len(sorted_data) - 1

    while low <= high:

        mid = (low + high) // 2
        current_value = sorted_data[mid][1].lower()

        if current_value == search_term:
            return sorted_data[mid]

        elif current_value < search_term:
            low = mid + 1

        else:
            high = mid - 1

    return None


# Quick sort
def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2][1].lower()

    left = []
    middle = []
    right = []

    for row in data:

        if len(row) < 2:
            continue

        value = row[1].lower()

        if value < pivot:
            left.append(row)
        elif value == pivot:
            middle.append(row)
        else:
            right.append(row)

    return quick_sort(left) + middle + quick_sort(right)


# Bubble sort (kept for comparison)
def bubble_sort(data):

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            if data[j][1].lower() > data[j + 1][1].lower():
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# MAIN PROGRAM
def main():

    if not hotdog_data:
        return

    results = analyse_data(hotdog_data)

    if results:
        save_results("analysis_output.txt", results)

    print("\nSorted Data (Quick Sort):")
    sorted_data = quick_sort(hotdog_data)

    for row in sorted_data:
        print(row)

    search_term = input("\nEnter search value: ")

    print("\nLinear Search Result:")
    print(linear_search(hotdog_data, search_term))

    print("\nBinary Search Result:")
    print(binary_search(hotdog_data, search_term))


# Run program
if __name__ == "__main__":
    main()
