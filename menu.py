def main():
    # --- Part 1: Initialize variables one by one ---
    menu = []      # List for current food items and their information
    orders = []    # List for customer order selections
    revenues = []  # List for daily sales and financial data
    ratings = []   # List for customer feedback scores
    
    # --- Part 2: Collection ---
    # We use this list to identify which options require staff authorization (password)
    staff_modules = ["1", "3"] # Producer upload and Revenue view require password

    # --- Part 3: System Header Output ---
    print("========== Main System ==========")
    print("Ann Cafe Booking System v1.0")
    print("Dev Team: Group 5")
    print("Last Update: 2026-4-12")
    print("---------------------------------")

    while True:
        # --- Part 4: Display Menu ---
        print("\nAvailable Options:")
        print("1. [Producer] Upload & Manage")
        print("2. [Consumer] Select & Order")
        print("3. [Producer] View Total Revenue")
        print("4. [Consumer] Rating System")
        print("0. Exit")
        
        # Get user input and remove extra spaces
        choice = input("\nYour choice: ").strip()

        # --- Part 5: Algorithm Logic ---
        # Check if the chosen module requires a producer password
        if choice in staff_modules:
            password = input("Enter Producer Password: ")
            if password != "ann123":
                print("Access Denied: Incorrect Password!")
                continue # Go back to main menu

        # Routing to different subroutines for each specific choice
        if choice == "1":
            menu = producer_approve_page()
        elif choice == "2":
            orders = consumer_selection_page(menu)
        elif choice == "3":
            revenues = total_revenue_page(orders)
        elif choice == "4":
            ratings = rating_scoring_page(menu)
        elif choice == "0":
            print("Shutting down system... Goodbye!")
            break
        else:
            print("Invalid option. Please choose 0-4.")

if __name__ == "__main__":
    main()
