def save_results(filename, most_productive, total_vegan, total_meat,
                 least_ketchup_vendor, most_ketchup_vendor,
                 most_onions_vendor, most_efficient_vendor,
                 least_efficient_vendor):
    """
    Saves the analysis results to a text file.
    """

    try:
        with open(filename, 'w') as file:

            file.write("=== HOTDOG ANALYSIS REPORT ===\n\n")

            file.write("Most Productive Vendor: " + str(most_productive) + "\n\n")

            file.write("Vegan vs Meat Totals:\n")
            file.write("Vegan: " + str(total_vegan) + "\n")
            file.write("Meat: " + str(total_meat) + "\n\n")

            file.write("Ketchup Usage:\n")
            file.write("Least: " + str(least_ketchup_vendor) + "\n")
            file.write("Most: " + str(most_ketchup_vendor) + "\n\n")

            file.write("Onion Usage:\n")
            file.write("Highest: " + str(most_onions_vendor) + "\n\n")

            file.write("Efficiency (Ketchup per Hotdog):\n")
            file.write("Most Efficient: " + str(most_efficient_vendor) + "\n")
            file.write("Least Efficient: " + str(least_efficient_vendor) + "\n")

        print("\nResults successfully saved to", filename)

    except Exception as e:
        print("Error saving file:", e)
