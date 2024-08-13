from cythontest.shopping_list import ShoppingList 

def test_shopping_list():
    list = ShoppingList()
    assert list.apples == 1
    assert list.bananas == 2
    assert list.eggs == 3
    assert list.milk_cartons == 4
