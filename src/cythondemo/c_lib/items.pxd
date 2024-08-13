cdef extern from "items.h":
    ctypedef struct ShoppingList:
        int apples
        int bananas
        int eggs
        int milk_cartons

    void print_shopping_list(ShoppingList *list)
    ShoppingList generate_shopping_list()

