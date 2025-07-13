
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User,		\
					Computer,	\
					Screen,		\
					Keyboard,	\
					Mouse,		\
					Inventory,	\
					Product

# --------------------------------------------------------------------- [ MAIN ]

def main():

############# Products ############

	inventory = Inventory()
	inventory.add_product(Computer("Lenovo i5", 2024, "i5-14400", "", 16, 512 ,  1100))
	inventory.add_product(Computer("Alienware Aurora", 2025, "i7-265F", "RTX 4060 Ti", 32 ,1000, 1800))
	inventory.add_product(Computer("Dell OptiPlex", 2024, "i7-14700", "", 16, 256, 1680))
	inventory.add_product(Screen("Compaq S710",16, False, 50))
	inventory.add_product(Screen("Samsung 27 FHD",27, True, 160))
	inventory.add_product(Screen("Samsung 24-inch FHD",24, True, 104))
	inventory.add_product(Screen("Acer 21.5 VA FHD Monitor",21.5, True, 105))
	inventory.add_product(Screen("Dell 24 Monitor - S2425H",24, True, 185))
	inventory.add_product(Keyboard("HP 150 Wired Keyboard", False, False, "100%", 25))
	inventory.add_product(Keyboard("Logitech Pebble Keys 2 K380s", True, False, "60%", 50))
	inventory.add_product(Keyboard("Gaming Keyboard", False, False, "100%", 28))
	inventory.add_product(Keyboard("MageGee Portable", True, True, "65%", 34))
	inventory.add_product(Mouse("Logitech M325s", True, 3, 20))
	inventory.add_product(Mouse("Anker Vertical Ergonomic", True, 5, 25))
	inventory.add_product(Mouse("Dell - MS116", False, 3, 22))
	inventory.add_product(Mouse("Logitech G502 Hero", False, 11, 55))

############ Users ############

	Karine = User("Karine")
	Bertrand = User("Bertrand")

############ Operations ############

	print("\n--- All Inventory ---")
	inventory.list_inventory()

	print("\n--- Giving to Karine  ---")
	item1 = inventory.search_by_name("Dell OptiPlex")
	item2 = inventory.search_by_price(105)
	item3 = inventory.search_keyboard_info(True, False)
	item4 = inventory.search_mouse(True, 3)
	item5 = inventory.search_by_name("The answer to life the universe and everything")
	inventory.give_to([item1, item2, item3, item4, item5, Product("Fake Product", 9999)], Karine)

	print("\n--- Giving to Bertrand ---")
	item_a = inventory.search_by_price(69)
	item_b = inventory.search_computer(32, 1000)
	item_c = inventory.search_monitor(27, True)
	item_d = inventory.search_by_name("Dell OptiPlex")
	item_e = inventory.search_keyboard_type("100%")
	item_f = inventory.search_mouse(False, 11)
	inventory.give_to([item_a, item_b, item_c, item_d, item_e, item_f], Bertrand)

	print("\n--- All Inventory After Giving ---")
	inventory.list_inventory()

	print("\n--- Quantity---")
	inventory.list_quantity()

	print("\n--- Values ---")
	inventory.list_values()

	print("\n--- Inventory of Karine ---")
	inventory.list_inventory_of_user(Karine)

	return ( 0 )

if __name__ == "__main__":
	main()
