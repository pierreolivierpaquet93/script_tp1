
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer, \
					Screen, \
					Keyboard, \
					Mouse, \
					Inventory

# --------------------------------------------------------------------- [ MAIN ]

def main():
	utilisateur = User( "NotSoRandom UserName" )
	ordinateur = Computer( "nom::ordinateur", 690, 2024, "CPU", "GPU", 4, 512 )
	ecran = Screen( "nom::ecran", 280, 16, True )

	clavier = Keyboard( "nom::clavier", 100, False, False, Keyboard.types["60%"] )
	clavier2 = Keyboard( "nom::clavier2", 250, False, True, Keyboard.types["100%"] )

	riz = User( "Original Name" )

	souris = Mouse( "nom::souris", 150, False, 6 )
	souris2 = Mouse( "nom::souris2", 73, False, 8 )

	inventaire = Inventory()
	inventaire.add_product( souris )
	inventaire.add_product( souris2 )
	inventaire.add_product( ecran )
	inventaire.add_product( clavier2 )
	inventaire.add_product( ordinateur )

	inventaire.add_product( clavier )

	item = inventaire.search_by_name( "nom::souris2" )
	item2 = inventaire.search_by_price( 73 )

	print( type( Screen ).__name__ )

	item3 = inventaire.search_by_monitor( 16, True )


	return ( 0 )

if __name__ == "__main__":
	main()
