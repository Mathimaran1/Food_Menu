def menu_serializer(menu):

    return {

        "id":str(menu["_id"]),
        "name":menu["name"],
        "category":menu["category"],
        "price":menu["price"],
        "description":menu["description"],
        "veg":menu["veg"],
        "spicy":menu["spicy"],
        "rating":menu["rating"]

    }



def menu_list_serializer(menu):

    return [

        menu_serializer(item)

        for item in menu

    ]



def category_serializer(category):

    return {

        "id":str(category["_id"]),
        "name":category["name"]

    }



def category_list_serializer(categories):

    return [

        category_serializer(item)

        for item in categories

    ]