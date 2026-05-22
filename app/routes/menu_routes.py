from fastapi import APIRouter, HTTPException, Form
from enum import Enum

from database import menu_collection, category_collection
from schemas.menu_schema import menu_serializer, menu_list_serializer, category_list_serializer

router = APIRouter()

class CategoryName(str, Enum):
    breakfast = "Breakfast"
    lunch = "Lunch"
    dinner = "Dinner"
    drinks = "Drinks"
    dessert = "Dessert"

@router.post("/menu")
def create_menu(
    name: str = Form(...),
    category: CategoryName = Form(...),
    price: int = Form(...),
    description: str = Form(...),
    veg: bool = Form(...),
    spicy: bool = Form(...),
    rating: float = Form(...)
):
    category_exists = category_collection.find_one({"name": category.value})
    if not category_exists:
        raise HTTPException(status_code=400, detail="Category does not exist.")

    next_id = str(menu_collection.count_documents({}) + 1)

    item_dict = {
        "_id": next_id,
        "name": name,
        "category": category.value,
        "price": price,
        "description": description,
        "veg": veg,
        "spicy": spicy,
        "rating": rating
    }
    menu_collection.insert_one(item_dict)
    
    return {"message": "Menu item added successfully", "id": next_id}

@router.get("/categories")
def get_categories():
    return category_list_serializer(category_collection.find())

@router.get("/menu")
def get_menu():
    return menu_list_serializer(menu_collection.find())

@router.get("/menu/{id}")
def get_menu_item(id: str):
    item = menu_collection.find_one({"_id": id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return menu_serializer(item)

@router.get("/menu/category/{id}")
def get_category_menu(id: str):
    category = category_collection.find_one({"_id": id})
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    menu = menu_collection.find({"category": category["name"]})
    return menu_list_serializer(menu)