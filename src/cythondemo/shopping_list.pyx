from .c_lib cimport items

class ShoppingList():
    def __init__(self):
        list = items.generate_shopping_list()
        self.apples = list.apples
        self.bananas = list.bananas
        self.eggs = list.eggs
        self.milk_cartons = list.milk_cartons

    def __str__(self):
        print(f"Apples: {self.apples}, Bananas: {self.bananas}, Eggs: {self.eggs}, Milk Cartons: {self.milk_cartons}")
