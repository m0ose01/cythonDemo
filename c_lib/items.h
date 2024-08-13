typedef struct
{
	int apples;
	int bananas;
	int eggs;
	int milk_cartons;
} ShoppingList;

void print_shopping_list(ShoppingList *list);
ShoppingList generate_shopping_list(void);
