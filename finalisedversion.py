import time
import copy


# Load data from file
def load_data(filename):

    hotdog_data = []

    try:
        with open(filename, 'r') as file:
            for line in file:

                items = line.strip().split(',')

                if len(items) != 7:
                    print("Skipping invalid row:", items)
                    continue

                hotdog_data.append(items)

    except FileNotFoundError:
        print("Error: file not found")
        return []

    return hotdog_data


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

    # Unmodified original data
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


# Quick sort function
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


# Bubble sort function
def bubble_sort(data):

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            if data[j][1].lower() > data[j + 1][1].lower():
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


# Analyse dataset
def analyse_data(data):

    if len(data) == 0:
        print("No data to analyse")
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

    most_productive = max(vendors, key=lambda v: vendors[v]["total"])

    total_vegan = sum(v["vegan"] for v in vendors.values())
    total_meat = sum(v["meat"] for v in vendors.values())

    least_ketchup = min(vendors, key=lambda v: vendors[v]["ketchup"])
    most_ketchup = max(vendors, key=lambda v: vendors[v]["ketchup"])

    most_onions = max(vendors, key=lambda v: vendors[v]["onions"])

    most_efficient = ""
    least_efficient = ""

    best = float("inf")
    worst = -1

    for vendor in vendors:

        if vendors[vendor]["total"] == 0:
            continue

        ratio = vendors[vendor]["ketchup"] / vendors[vendor]["total"]

        if ratio < best:
            best = ratio
            most_efficient = vendor

        if ratio > worst:
            worst = ratio
            least_efficient = vendor

    print("\nHotdog Analysis Report")
    print("Most Productive:", most_productive)
    print("Vegan Total:", total_vegan)
    print("Meat Total:", total_meat)
    print("Least Ketchup:", least_ketchup)
    print("Most Ketchup:", most_ketchup)
    print("Most Onions:", most_onions)
    print("Most Efficient:", most_efficient)
    print("Least Efficient:", least_efficient)

    return (most_productive, total_vegan, total_meat,
            least_ketchup, most_ketchup,
            most_onions, most_efficient, least_efficient)


# Save results to file
def save_results(filename, most_productive, total_vegan, total_meat,
                 least_ketchup, most_ketchup,
                 most_onions, most_efficient,
                 least_efficient):

    try:
        with open(filename, 'w') as file:

            file.write("Hotdog Analysis Report\n")
            file.write("======================\n\n")

            file.write("Most Productive: " + str(most_productive) + "\n\n")
            file.write("Vegan Total: " + str(total_vegan) + "\n")
            file.write("Meat Total: " + str(total_meat) + "\n\n")

            file.write("Least Ketchup: " + str(least_ketchup) + "\n")
            file.write("Most Ketchup: " + str(most_ketchup) + "\n\n")

            file.write("Most Onions: " + str(most_onions) + "\n\n")

            file.write("Most Efficient: " + str(most_efficient) + "\n")
            file.write("Least Efficient: " + str(least_efficient) + "\n")

        print("Results saved")

    except Exception as e:
        print("Error saving file:", e)


# Main program
def main():

    hotdog_data = load_data("Hotdog.txt")

    if not hotdog_data:
        return

    # Sorting inside main (fixed structure)
    sorted_data = quick_sort(hotdog_data)

    print("\nSorted Data:")
    for row in sorted_data:
        print(row)

    results = analyse_data(hotdog_data)

    if results:
        save_results("analysis_output.txt", *results)

    search_term = input("\nEnter search value: ")

    print("\nLinear Search Result:")
    print(linear_search(hotdog_data, search_term))

    print("\nBinary Search Result:")
    print(binary_search(hotdog_data, search_term))


# Run program safely
if __name__ == "__main__":
    main()
