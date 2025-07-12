
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer, \
					Screen, \
					Keyboard, \
					Mouse

# --------------------------------------------------------------------- [ MAIN ]

def main():
	utilisateur = User( "Diego l'Ortho" )
	ordinateur = Computer( "Nom::Ordinateur", 690, utilisateur, 2024, "Caliss", "Tabarnack", 4, 512 )
	ecran = Screen( "Nom::ecran", 280, utilisateur, 16, True )
	print( type( ecran ) )

	clavier2 = Keyboard( "Keycron", 250, utilisateur, False, True, Keyboard.types["100%"] )

	riz = User( "Rizuto Bazmatii" )
	souris = Mouse( "Nom::Souris", 150, riz, False, 6 )

	return ( 0 )

if __name__ == "__main__":
	main()
