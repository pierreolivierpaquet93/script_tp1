
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
	ordinateur = Computer( "nom::ordinateur", 690, utilisateur, 2024, "CPU", "GPU", 4, 512 )
	ecran = Screen( "nom::ecran", 280, utilisateur, 16, True )

	clavier = Keyboard( "nom::clavier", 100, utilisateur, False, False, Keyboard.types["60%"] )
	clavier2 = Keyboard( "nom::clavier2", 250, utilisateur, False, True, Keyboard.types["100%"] )

	riz = User( "Original Name" )

	souris = Mouse( "nom::souris", 150, riz, False, 6 )
	souris2 = Mouse( "nom::souris2", 73, utilisateur, False, 8 )

	inventaire = Inventory()
	inventaire.add_product( souris )
	inventaire.add_product( souris2 )
	inventaire.add_product( ecran )
	inventaire.add_product( clavier2 )
	inventaire.add_product( ordinateur )

	inventaire.add_product( clavier )

	item = inventaire.search_by_name( "nom::souris2" )
	item2 = inventaire.search_by_price( 73 )

	return ( 0 )

if __name__ == "__main__":
	main()
