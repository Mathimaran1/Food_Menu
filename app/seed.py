import os
import sys

# Ensure app directory is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import db, menu_collection, category_collection

def seed_database():
    print("Clearing existing collections...")
    menu_collection.drop()
    category_collection.drop()

    categories = [
        {"_id": "1", "name": "Breakfast"},
        {"_id": "2", "name": "Lunch"},
        {"_id": "3", "name": "Dinner"},
        {"_id": "4", "name": "Drinks"},
        {"_id": "5", "name": "Dessert"}
    ]

    print("Inserting categories...")
    category_collection.insert_many(categories)

    menu_items = [
        {
            "_id": "1",
            "name": "Idly",
            "category": "Breakfast",
            "description": "Fluffy, cloud-like rice cakes served warm with delicious coconut chutney and fresh sambar.",
            "price": 2.50,
            "rating": 4.8,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "2",
            "name": "Dosa",
            "category": "Breakfast",
            "description": "A thin, crispy golden crepe filled with a gentle, mildly spiced potato mash.",
            "price": 4.00,
            "rating": 4.9,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "3",
            "name": "Veg Meals",
            "category": "Lunch",
            "description": "A wholesome traditional meal with rice, dal, fresh vegetables, and sweet payasam to finish.",
            "price": 6.50,
            "rating": 4.7,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "4",
            "name": "Chicken Biryani",
            "category": "Lunch",
            "description": "Aromatic basmati rice cooked perfectly with tender chicken pieces and rich, flavourful spices.",
            "price": 8.00,
            "rating": 4.9,
            "veg": False,
            "spicy": True
        },
        {
            "_id": "5",
            "name": "Chapati",
            "category": "Dinner",
            "description": "Warm, homely wheat flatbreads brushed lightly with fresh butter.",
            "price": 1.50,
            "rating": 4.6,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "6",
            "name": "Paneer Butter Masala",
            "category": "Dinner",
            "description": "Soft cubes of paneer gently simmered in a rich, sweet, and creamy tomato gravy.",
            "price": 6.00,
            "rating": 4.8,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "7",
            "name": "Chettinad Chicken",
            "category": "Dinner",
            "description": "A lovely, fiery chicken curry made with roasted spices for those who love a good kick.",
            "price": 7.50,
            "rating": 4.5,
            "veg": False,
            "spicy": True
        },
        {
            "_id": "8",
            "name": "Lassi",
            "category": "Drinks",
            "description": "A cool, thick, and sweet yogurt drink blended with a lovely hint of cardamom.",
            "price": 2.50,
            "rating": 4.9,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "9",
            "name": "Masala Chai",
            "category": "Drinks",
            "description": "Comforting hot tea brewed beautifully with milk, ginger, and warming spices.",
            "price": 1.50,
            "rating": 5.0,
            "veg": True,
            "spicy": False
        },
        {
            "_id": "10",
            "name": "Gulab Jamun",
            "category": "Dessert",
            "description": "Two soft, melt-in-the-mouth milk dumplings soaked in a sweet, sticky sugar syrup.",
            "price": 3.00,
            "rating": 4.9,
            "veg": True,
            "spicy": False
        }
    ]

    print("Inserting menu items...")
    menu_collection.insert_many(menu_items)

    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
