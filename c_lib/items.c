#include <stdio.h>
#include "items.h"

void print_shopping_list(ShoppingList *list)
{
	printf("Apples: %i\nBananas: %i\nEggs: %i\nMilk Cartons: %i\n", list->apples, list->bananas, list->eggs, list->milk_cartons);
}

ShoppingList generate_shopping_list(void)
{
	ShoppingList list = {1, 2, 3, 4};
	return list;
}
