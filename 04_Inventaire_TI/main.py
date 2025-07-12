
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer, \
					Screen, \
					Keyboard, \
					Mouse, \
					Inventory

# --------------------------------------------------------------------- [ MAIN ]

def main():
	inventaire = Inventory()
	inventaire.add_product( Mouse( "nom::souris", 98, True, 4 ) )
	inventaire.search_by_keyboard_info( True, False )
	inventaire.list_quantity()
	return ( 0 )

if __name__ == "__main__":
	main()
