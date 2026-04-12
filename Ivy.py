def consumer_selection_page(menu_array):
    order_array = []
    
    print("\n===== Consumer Selection Page =====")
    if len(menu_array) == 0:
        print("Menu is empty!")
        return order_array
    
    print("\n--- Menu (0-1 not spicy, 2-3 spicy) ---")
    for dish in menu_array:
        print(f"{dish[0]:<15} ${dish[1]:.2f}  Spiciness: {dish[2]}")
    
    while True:
        choice = input("\nEnter dish name to order (or 'done' to checkout): ").strip()
        if choice.lower() == "done":
            break
        
        found = False
        for dish in menu_array:
            if dish[0].lower() == choice.lower():
                order_array.append([dish[0], dish[1]])
                print(f"Ordered: {dish[0]}, Price: {dish[1]}")
                found = True
                break
        if not found:
            print("Dish not found.")
    
    return order_array
