
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer, \
					Screen

# --------------------------------------------------------------------- [ MAIN ]

def main():
	utilisateur = User( "Diego l'Ortho" )
	ordinateur = Computer( "Nom::Ordinateur", 690, utilisateur, 2024, "Caliss", "Tabarnack", 4, 512 )
	ecran = Screen( "Nom::ecran", 280, utilisateur, 16, True )
	print( type( ecran ) )
	return ( 0 )

if __name__ == "__main__":
	main()