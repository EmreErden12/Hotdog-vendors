hotdog_data = []

# Load data from file
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

    # Return all results so they can be saved
    return (most_productive, total_vegan, total_meat,
            least_ketchup_vendor, most_ketchup_vendor,
            most_onions_vendor, most_efficient_vendor,
            least_efficient_vendor)


# Save results function
def save_results(filename, results):

    try:
        with open(filename, 'w') as file:
