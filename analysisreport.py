def load_data(filename):
    """
    This function reads the file and converts each line into a list.
    Each row in the file represents one record of sales data.
    """

    hotdog_data = []

    try:
        with open(filename, 'r') as file:
            for line in file:

                # Remove extra spaces and split the line into separate values
                items = line.strip().split(',')

                # Check that the row has the correct number of values
                # This prevents errors later in the program
                if len(items) != 7:
                    print("Skipping invalid row:", items)
                    continue

                # Add cleaned row into main dataset list
                hotdog_data.append(items)

    except FileNotFoundError:
        # This runs if the file name is wrong or file does not exist
        print("Error: File not found. Please check the file name.")
        return []

    except Exception as e:
        # Handles any unexpected errors when reading the file
        print("Unexpected error while reading file:", e)
        return []

    return hotdog_data


def analyse_data(data):
    """
    This function analyses the hotdog dataset.

    It calculates:
    - Which vendor sold the most hotdogs
    - Total vegan vs meat hotdogs sold
    - Which vendor uses the most and least ketchup
    - Which vendor uses the most onions
    - How efficient each vendor is based on ketchup usage
    """

    # If there is no data, stop the function
    if len(data) == 0:
        print("No data available to analyse.")
        return

    vendors = {}

    #STEP 1: PROCESS EACH ROW IN THE DATASET
    for row in data:

        try:
            # Extract values from each column
            vendor = row[1]
            vegan = int(row[3])
            meat = int(row[4])
            onions = float(row[5])
            ketchup = float(row[6])

        except ValueError:
            # If data is not in correct format, skip that row
            print("Skipping invalid data row:", row)
            continue

        # Total hotdogs sold in this row
        total = vegan + meat

        # If this vendor has not been seen before, create a new record
        if vendor not in vendors:
            vendors[vendor] = {
                "vegan": 0,
                "meat": 0,
                "total": 0,
                "onions": 0,
                "ketchup": 0
            }

        # Add current row values to the vendor totals
        vendors[vendor]["vegan"] += vegan
        vendors[vendor]["meat"] += meat
        vendors[vendor]["total"] += total
        vendors[vendor]["onions"] += onions
        vendors[vendor]["ketchup"] += ketchup

    # STEP 2: FIND MOST PRODUCTIVE VENDOR
    most_productive = ""
    highest_total = -1

    for vendor in vendors:

        # Compare each vendor's total sales
        if vendors[vendor]["total"] > highest_total:
            highest_total = vendors[vendor]["total"]
            most_productive = vendor

    # STEP 3: CALCULATE TOTAL VEGAN AND MEAT SALES
    total_vegan = 0
    total_meat = 0

    for vendor in vendors:
        total_vegan += vendors[vendor]["vegan"]
        total_meat += vendors[vendor]["meat"]

    #STEP 4: FIND KETCHUP USAGE EXTREMES
    least_ketchup_vendor = ""
    most_ketchup_vendor = ""
    least_ketchup = float("inf")
    most_ketchup = -1

    for vendor in vendors:

        ketchup_total = vendors[vendor]["ketchup"]

        # Find vendor using the least ketchup overall
        if ketchup_total < least_ketchup:
            least_ketchup = ketchup_total
            least_ketchup_vendor = vendor

        # Find vendor using the most ketchu overall
        if ketchup_total > most_ketchup:
            most_ketchup = ketchup_total
            most_ketchup_vendor = vendor

    # STEP 5: FIND ONION USAGE
    most_onions_vendor = ""
    most_onions = -1

    for vendor in vendors:

        # Compare onion usage betwee vendors
        if vendors[vendor]["onions"] > most_onions:
            most_onions = vendors[vendor]["onions"]
            most_onions_vendor = vendor

    # STEP 6: CALCULATE EFFICIENCY
    most_efficient_vendor = ""
    least_efficient_vendor = ""
    best_ratio = float("inf")
    worst_ratio = -1

    for vendor in vendors:

        # Avoid dividing by zero if a vendor has no sales
        if vendors[vendor]["total"] == 0:
            continue

        # Efficiency = ketchup used per hotdog sold
        ratio = vendors[vendor]["ketchup"] / vendors[vendor]["total"]

        # Find most efficient (lowest ketchup usage)
        if ratio < best_ratio:
            best_ratio = ratio
            most_efficient_vendor = vendor

        # Find least efficient (highest ketchup usage)
        if ratio > worst_ratio:
            worst_ratio = ratio
            least_efficient_vendor = vendor

    # FINAL OUTPUT SECTIO
    print("\nHOTDOG ANALYSIS REPORT\n")

    print("1. Most Productive Vendor:", most_productive)

    print("\n2. Vegan vs Meat Totals:")
    print("   Vegan:", total_vegan)
    print("   Meat:", total_meat)

    print("\n3. Ketchup Usage:")
    print("   Least:", least_ketchup_vendor)
    print("   Most:", most_ketchup_vendor)

    print("\n4. Onion Usage:")
    print("   Highest:", most_onions_vendor)

    print("\n5. Efficiency (Ketchup per Hotdog):")
    print("   Most Efficient:", most_efficient_vendor)
    print("   Least Efficient:", least_efficient_vendor)


# RUN PROGRAM
data = load_data("Hotdog.txt")
analyse_data(data)
