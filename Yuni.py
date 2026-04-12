def producer_upload_page():# define a subroutine
    menu_array = []
    # Collection (array) used to store multiple menu items
    # Data abstraction: simplifies managing many dishes
    
    print("===== Producer Upload Page =====")
    # output the subtitle

    while True:# iteration
        name = input("Enter dish name (or 'done' to finish): ")# input dish name from producer

        if name.lower() == "done":
        # selection(check if exit)
            break# jump out of the iteration

        price_str = input(f"Enter price for {name}: ")
        # Check price is a valid number
        
        if price_str.replace(".", "").isdigit() and price_str.count(".") <= 1:
        # Check if it looks like a number (with one decimal point allowed)
            price = float(price_str)
        else:# invalid input
            print("Error: Please enter a valid number.")
            continue# continue the iteration(keep asking)

        spice_str = input(f"Enter spiciness 0-3 for {name}: ")# input spiciness from producer

        if spice_str.isdigit():# Check spiciness is integer
            spice = int(spice_str)
            # compulsory turn into integer
        else:# invalid input
            print("Error: Please enter a valid number.")
            continue# continue the iteration(keep asking)

        if 0 <= spice <= 3:# Check spiciness range
            menu_array.append([name, price, spice])
            # add this into the menu_array
            print(f"Added: {name}, Price: {price}, Spiciness: {spice}")
            # output the dish name, price and spiciness
        else:# invalid input
            print("Error: Spiciness must be between 0 and 3.")

    return menu_array# return the menu producer upload to the main program
