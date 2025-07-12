
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer, \
					Screen, \
					Keyboard

# --------------------------------------------------------------------- [ MAIN ]

def main():
	utilisateur = User( "Diego l'Ortho" )
	ordinateur = Computer( "Nom::Ordinateur", 690, utilisateur, 2024, "Caliss", "Tabarnack", 4, 512 )
	ecran = Screen( "Nom::ecran", 280, utilisateur, 16, True )
	print( type( ecran ) )

	clavier = Keyboard( True, False, (666000, "Evil MegaBoard") )
	clavier2 = Keyboard( False, True, Keyboard.types[100] )

	return ( 0 )

if __name__ == "__main__":
	main()