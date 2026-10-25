inventory = {}

def add_product(name, quantity):
    inventory[name] = quantity

def update_product(name, quantity):
    if name in inventory:
        inventory[name] = quantity
    else:
        print("Product not found")

def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]

add_product("Pen", 10)
add_product("Book", 20)
add_product("Pencil", 5)

update_product("Pen", 15)

print("Inventory:", inventory)
print("Highest Stock:", max(inventory, key=inventory.get))
remove_product("Pencil")
print("Total Products:", len(inventory))
print("Updated Inventory:", inventory)