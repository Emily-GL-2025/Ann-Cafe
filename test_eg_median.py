
import emilyguo as eg

menu = {
        "pizza": {
            "name": "Pepperoni Pizza Slice",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [5, 3, 4, 3, 4, 4, 4, 4, 3, 3, 4, 5, 4, 4, 5]
        },
         "pizza2": {
            "name": "Pepperoni Pizza Slice2",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": []
        },
        "pizza3": {
            "name": "Pepperoni Pizza Slice2",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [1, 3]
        },
        "pizza4": {
            "name": "Pepperoni Pizza Slice2",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [1, 3, 2]
        },
        "pizza5": {
            "name": "Pepperoni Pizza Slice2",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [1, 3, 2, 5]
        },
        "rice": {
            "name": "Beef and Rice",
            "price": 5.50,
            "description": "Beef with carrot and rice.", 
            "photo": "https://images.unsplash.com/photo-1573403707391-3612fb5e1f38?w=500&q=80",
            "ratings": [2, 3, 4, 4, 4, 4, 5, 2, 1, 4, 2, 3, 4, 5, 3]
        }
}

for items_id, details in menu.items():
    print(details["ratings"])
    print("Sorted:",sorted(details["ratings"]))
    print("median rating: ", eg.median_calculation(details["ratings"]))
