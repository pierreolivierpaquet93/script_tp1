
# ----------------------------------------------------------------- [ MODULE.S ]

from data import User, Product, Computer, Screen, Keyboard

# --------------------------------------------------------------------- [ MAIN ]

def main() -> int:

	item = Product( "Fake", 9999 )
	item0 = Computer( "ordinateur", 2020, "intel", "nvidia", 8, 512, 1200 )
	item1 = Screen( "ecran", 16.5, True, 1000 )
	item3 = Keyboard( "clavier", True, False, "75%", 100 )

	return ( 0 )

if __name__ == "__main__":
	main()
