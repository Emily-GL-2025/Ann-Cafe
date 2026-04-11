import streamlit as st
import emilyguo as eg

# ---------------------------------------------------------
# 1. Initialize Session State & Mock Data
# ---------------------------------------------------------
# Set page configuration
st.set_page_config(page_title="School Cafeteria", page_icon="🍔", layout="centered")

# Track which page we are on: "home", "detail", "checkout", or "owner"
if "page" not in st.session_state:
    st.session_state.page = "home"

# Track which item was clicked
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

# Initialize shopping cart (stores item_id and quantity)
if "cart" not in st.session_state:
    st.session_state.cart = {}  # Format: {"burger": 2, "pizza": 1}

# Owner password (can be changed to more secure method later)
if "owner_password" not in st.session_state:
    st.session_state.owner_password = "1111"

# Initialize the menu data (using session state so new ratings are saved)
if "menu" not in st.session_state:
    st.session_state.menu = {
        "burger": {
            "name": "Classic Cheeseburger",
            "price": 5.50,
            "description": "A juicy beef patty topped with melted cheese, lettuce, and our secret sauce.",
            "photo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&q=80",
            "ratings": [4, 5, 4, 3, 5, 3, 4, 4, 5, 3, 5, 3, 2, 4, 4]
        },
        "pizza": {
            "name": "Pepperoni Pizza Slice",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [5, 3, 4, 3, 4, 4, 4, 4, 3, 3, 4, 5, 4, 4, 5]
        },
        "salad": {
            "name": "Chicken Caesar Salad",
            "price": 4.50,
            "description": "Crisp romaine lettuce, grilled chicken, croutons, and parmesan cheese.",
            "photo": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=500&q=80",
            "ratings": [4, 4, 5, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 3, 4]
        },
        # code developed by Emily 04/10
        "rice": {
            "name": "Beef and Rice",
            "price": 5.50,
            "description": "A warm dish of tender beef served over fluffy rice with sweet carrots, creating a comforting blend of savory and natural flavors.", 
            "photo": "https://images.unsplash.com/photo-1573403707391-3612fb5e1f38?w=500&q=80",
            "ratings": [4, 4, 5]
        }
        # end of the code developed by Emily
    }

# Helper function to calculate average ratings
def get_average_rating(ratings):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)

# Helper function to get total items in cart
def get_cart_count():
    return sum(st.session_state.cart.values())

# Helper function to calculate cart total price
def get_cart_total():
    total = 0
    for item_id, quantity in st.session_state.cart.items():
        total += st.session_state.menu[item_id]["price"] * quantity
    return total

# Navigation callbacks
def go_to_detail(item_id):
    st.session_state.selected_item = item_id
    st.session_state.page = "detail"

def go_to_home():
    st.session_state.selected_item = None
    st.session_state.page = "home"

def go_to_checkout():
    st.session_state.page = "checkout"

def go_to_owner():
    st.session_state.page = "owner"

# Cart management functions
def add_to_cart(item_id):
    if item_id in st.session_state.cart:
        st.session_state.cart[item_id] += 1
    else:
        st.session_state.cart[item_id] = 1

def remove_from_cart(item_id):
    if item_id in st.session_state.cart:
        if st.session_state.cart[item_id] > 1:
            st.session_state.cart[item_id] -= 1
        else:
            del st.session_state.cart[item_id]

def clear_cart():
    st.session_state.cart = {}

# ---------------------------------------------------------
# 2. Home Page View
# ---------------------------------------------------------
if st.session_state.page == "home":
    # Header with shopping cart icon
    col_title, col_cart = st.columns([3, 1])
    with col_title:
        st.title("🏫 Cafeteria Menu")
    with col_cart:
        cart_count = get_cart_count()
        st.markdown(f"### 🛒 Cart: {cart_count}")
        if cart_count > 0:
            st.button("🛍️ Checkout", key="checkout_btn", on_click=go_to_checkout, width="stretch")
    
    st.write("Welcome! Click 'View Details' to see more about an item or leave a review.")
    
    st.divider()

    # code developed by Emily 04/10
    # set up bubble sort initial value for highest bayesian rating
    highest_bayesian_rating = -1
    highest_bayesian_rating_name = " "
    # end of the code developed by Emily

    # Loop through the menu items and display them
    for item_id, details in st.session_state.menu.items():
        # Use columns to lay out the photo next to the text
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(details["photo"], width="stretch")
            
        with col2:
            st.subheader(details["name"])
            st.write(f"**Price:** ${details['price']:.2f}")
            st.write(details["description"])
            
            avg_rating = get_average_rating(details["ratings"])
            # Display stars based on the rounded average rating
            st.write(f"**Rating:** {'⭐' * round(avg_rating)} ({avg_rating:.1f}/5 from {len(details['ratings'])} reviews)")
            
            #code developed by Emily 04/10
            bayesian_rating = eg.bayesian_average_calc(details["ratings"])
            # always keeps the highest bayesian rating and the corresponding item name
            if bayesian_rating > highest_bayesian_rating:
                highest_bayesian_rating = bayesian_rating
                highest_bayesian_rating_name = details["name"]
            # end of the code developed by Emily

            # Buttons row
            btn_col1, btn_col2, btn_col3 = st.columns([2, 2, 1])
            with btn_col1:
                st.button("View Details", key=f"btn_{item_id}", on_click=go_to_detail, args=(item_id,), width="stretch")
            with btn_col2:
                if st.button("➕ Add to Cart", key=f"add_{item_id}", width="stretch"):
                    add_to_cart(item_id)
                    st.rerun()
            with btn_col3:
                # Show quantity if item is in cart
                if item_id in st.session_state.cart:
                    st.write(f"**x{st.session_state.cart[item_id]}**")
            
        st.divider()
    
    # Chef's Recommended coded by Emily 04/10 using bayesian average
    st.info(f"👨‍🍳 Chef's Recommended (based on bayesian average): {highest_bayesian_rating_name}")
    # End of Emily's code

    # Trending Now coded by Emily 04/06 using buzz score
    #st.info("📈 Trending Now: [Coming soon ...] ")
    # End of Emily's code

    # Owner button moved to bottom of home page
    st.markdown("---")
    st.button("🔐 Add New Dish (Owner)", key="owner_btn", on_click=go_to_owner, width="stretch")

# ---------------------------------------------------------
# 3. Detail Page View
# ---------------------------------------------------------
elif st.session_state.page == "detail":
    # Get the data for the selected item
    item_id = st.session_state.selected_item
    item = st.session_state.menu[item_id]

    # Back button
    st.button("← Back to Menu", on_click=go_to_home)
    
    st.title(item["name"])

    # Item details
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.image(item["photo"], width="stretch")
    with col2:
        st.write(f"**Price:** ${item['price']:.2f}")
        st.write(item["description"])
        avg_rating = get_average_rating(item["ratings"])
        st.write(f"**Average Rating:** {'⭐' * round(avg_rating)} ({avg_rating:.1f}/5)")
        # Code added by Emily 04/09 using median function
        median_rating = eg.median_calculation(item["ratings"])
        st.write(f"**Median Rating:** {'⭐' * round(median_rating)} ({median_rating:.1f}/5)")
        # end of code added by Emily 04/09

    st.divider()

    # Add a new rating section
    st.subheader("Add a Rating")
    # Use a form so the app doesn't reload until the user hits "Submit"
    with st.form(key="rating_form"):
        new_rating = st.slider("Rate this item (1-5 stars)", min_value=1, max_value=5, value=5)
        submit_button = st.form_submit_button("Submit Rating")

        if submit_button:
            # Append the new rating to the session state
            st.session_state.menu[item_id]["ratings"].append(new_rating)
            st.success("Thank you for your rating!")
            # Rerun the app to update the UI with the new data
            st.rerun()

    st.divider()

    # List all previous ratings
    st.subheader("Previous Ratings")

    # code developed by Emily 04/10
    # Bar chart by Emily 04/10
    st.title("📊 Ratings Histogram")
    st.bar_chart(eg.histogram_calc(item["ratings"]))
    # End of the code developed by Emily
    
    if not item["ratings"]:
        st.info("No ratings yet. Be the first to rate!")
    else:
        # Reverse the list so the newest ratings show up first
        for i, rating in enumerate(reversed(item["ratings"])):
            st.write(f"**Review {len(item['ratings']) - i}:** {'⭐' * rating}")

# ---------------------------------------------------------
# 4. Checkout Page
# ---------------------------------------------------------
elif st.session_state.page == "checkout":
    st.title("🛍️ Checkout")
    
    # Back button
    st.button("← Back to Menu", on_click=go_to_home)
    
    if not st.session_state.cart:
        st.info("Your cart is empty! Go back to add some delicious items.")
    else:
        st.subheader("Your Order:")
        
        # Display each item in cart
        total = 0
        for item_id, quantity in st.session_state.cart.items():
            item = st.session_state.menu[item_id]
            item_total = item["price"] * quantity
            total += item_total
            
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.write(f"**{item['name']}**")
            with col2:
                st.write(f"${item['price']:.2f}")
            with col3:
                st.write(f"x {quantity}")
            with col4:
                st.write(f"**${item_total:.2f}**")
                if st.button("🗑️", key=f"remove_{item_id}"):
                    remove_from_cart(item_id)
                    st.rerun()
        
        st.divider()
        
        # Total
        st.subheader(f"**Total: ${total:.2f}**")
        
        st.divider()
        
        # Order button
        if st.button("✅ Place Order", type="primary", width="stretch"):
            st.success(f"🎉 Order placed successfully! Total: ${total:.2f}")
            st.balloons()
            clear_cart()
            st.write("Redirecting to home page...")
            import time
            time.sleep(2)
            go_to_home()
            st.rerun()

# ---------------------------------------------------------
# 5. Owner Page - Add New Dish (with Password Protection)
# ---------------------------------------------------------
elif st.session_state.page == "owner":
    st.title("👨‍🍳 Add New Dish to Menu")
    
    # Back button
    st.button("← Back to Menu", on_click=go_to_home)
    
    st.write("Fill in the details below to add a new dish to the cafeteria menu:")
    
    with st.form(key="add_dish_form"):
        # Password field (added at the top for security)
        st.subheader("🔐 Owner Authentication")
        owner_password_input = st.text_input("Owner Password", 
                                             type="password", 
                                             placeholder="Enter owner password")
        
        st.divider()
        
        # Input fields for new dish
        st.subheader("📝 Dish Information")
        dish_id = st.text_input("Dish ID (unique, lowercase, no spaces)", 
                                placeholder="e.g., pasta, sandwich")
        dish_name = st.text_input("Dish Name", 
                                  placeholder="e.g., Spaghetti Carbonara")
        dish_price = st.number_input("Price ($)", 
                                     min_value=0.0, 
                                     max_value=100.0, 
                                     value=5.0, 
                                     step=0.5)
        dish_description = st.text_area("Description", 
                                       placeholder="Describe the dish...")
        dish_photo = st.text_input("Photo URL", 
                                   value="https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&q=80",
                                   placeholder="Enter image URL")
        
        submit_dish = st.form_submit_button("Add Dish to Menu", type="primary")
        
        if submit_dish:
            # First check password
            if owner_password_input != st.session_state.owner_password:
                st.error("❌ Incorrect password! Access denied.")
            # Then validate other fields
            elif not dish_id or not dish_name or not dish_description:
                st.error("Please fill in all required fields!")
            elif dish_id in st.session_state.menu:
                st.error(f"Dish ID '{dish_id}' already exists! Please use a unique ID.")
            elif " " in dish_id:
                st.error("Dish ID cannot contain spaces!")
            else:
                # Add new dish to menu
                st.session_state.menu[dish_id] = {
                    "name": dish_name,
                    "price": dish_price,
                    "description": dish_description,
                    "photo": dish_photo,
                    "ratings": []
                }
                st.success(f"✅ '{dish_name}' has been added to the menu!")
                st.write("Redirecting to home page...")
                import time
                time.sleep(2)
                go_to_home()
                st.rerun()
    
    # Hint for testing (remove in production)
    st.info("💡 Hint for testing: Default password is '1111'")