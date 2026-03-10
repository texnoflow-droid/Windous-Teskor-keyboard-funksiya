
from collections import namedtuple


Dori = namedtuple('Dori', ('model', 'country', 'price', "Qollanishi"))

database = []

def add_item(model, country, price, qollanishi):
    new_item = Dori(model, country, price, qollanishi)
    database.append(new_item)
    print(f"Item {model} added successfully!")


def view_all_items():
    if not database:
        print("Database is empty.")
    else:
        for i, item in enumerate(database, start=1):
            print(f"Item {i}: {item}")


def search_by_model(model):
    found = False
    for item in database:
        if item.model.lower() == model.lower():
            print(item)
            found = True
    if not found:
        print(f"No item with model {model} found.")


def update_item(model, new_model, country, price, qollanishi):
    for item in database:
        if item.model.lower() == model.lower():
            index = database.index(item)
            database[index] = Dori(new_model, country, price, qollanishi)
            print(f"Item {model} updated successfully!")
            return
    print(f"No item with model {model} found.")


def delete_item(model):
    for item in database:
        if item.model.lower() == model.lower():
            database.remove(item)
            print(f"Item {model} deleted successfully!")
            return
    print(f"No item with model {model} found.")

while True:
    print("\n1. Add item")
    print("2. Dorilarni korish")
    print("3. Qidirish")
    print("4. Dori qo'shish")
    print("5. Dori ochirish")
    print("6. Chiqish ")
    choice = input("Choose an option: ")
    
