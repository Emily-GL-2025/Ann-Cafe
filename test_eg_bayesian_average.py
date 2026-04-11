# test script for etsting function bayesian_average_calc 
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
            "name": "Pepperoni Pizza Slice",
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
            "name": "Pepperoni Pizza Slice3",
            "price": 3.00,
            "description": "A large slice of classic New York style pepperoni pizza.",
            "photo": "https://images.unsplash.com/photo-1628840042765-356cda07504e?w=500&q=80",
            "ratings": [1, 3, 2]
        },
        "pizza5": {
            "name": "Pepperoni Pizza Slice4",
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
            "ratings": [4, 4, 5]
        },
        "burger": {
            "name": "Classic Cheeseburger",
            "price": 5.50,
            "description": "A juicy beef patty topped with melted cheese, lettuce, and our secret sauce.",
            "photo": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500&q=80",
            "ratings": [4, 5, 4, 3, 5, 3, 4, 4, 5, 3, 5, 3, 2, 4, 4]
        },
        "salad": {
            "name": "Chicken Caesar Salad",
            "price": 4.50,
            "description": "Crisp romaine lettuce, grilled chicken, croutons, and parmesan cheese.",
            "photo": "https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=500&q=80",
            "ratings": [4, 4, 5, 3, 4, 4, 2, 3, 4, 5, 3, 4, 4, 3, 4]
        }
}

for items_id, details in menu.items():
    print(details["name"])
    print(details["ratings"])
    if len(details["ratings"]) == 0:
        print("No ratings")
    else:
        print("Average: ", sum(details["ratings"])/len(details["ratings"]))
    print("bayesian average: ", eg.bayesian_average_calc(details["ratings"]))