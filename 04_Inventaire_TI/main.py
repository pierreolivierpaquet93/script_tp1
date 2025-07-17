
# ----------------------------------------------------------------- [ MODULE.S ]

from data import Inventory, User, Product, Computer, Screen, Keyboard

# --------------------------------------------------------------------- [ MAIN ]

def main() -> int:

	item = Product( "Fake", 9999 )
	item0 = Computer("Dell OptiPlex", 2024, "i7-14700", "", 16, 256, 1680)
	item1 = Screen( "ecran", 16.5, True, 1000 )
	item3 = Keyboard( "clavier", True, False, "75%", 100 )
	item4 = Keyboard( "clavier2", False, True, "0%", 3000 )

	inventaire = Inventory()
	inventaire.add_product( item3 )

	print( item0 )
	print( item1 )

	return ( 0 )

if __name__ == "__main__":
	main()
