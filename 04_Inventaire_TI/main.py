
# ----------------------------------------------------------------- [ MODULE.S ]

from Data import	User, \
					Computer

# --------------------------------------------------------------------- [ MAIN ]

def main():
	utilisateur = User( "Diego l'Ortho" )
	ordinateur = Computer( "Nom::Ordinateur", 690, utilisateur, 2024, "Caliss", "Tabarnack", 4, 512 )
	return ( 0 )

if __name__ == "__main__":
	main()