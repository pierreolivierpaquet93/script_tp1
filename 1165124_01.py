'''
[ ]	Ne pas utiliser de librairie externe
[ ]	Demandez une phrase en entrée
[ ]	Vous devez passer vérifier chaque lettre et les traités selon les
	conditions;
	[ ]	Si le caractère est un "-", vous devez remplacer le prochain caractère
		selon cette table de conversion:
		.----------------------.---------------------.
		| CARACTÈRE DU MESSAGE | CARACTÈRE RÉSULTANT |
		|----------------------+---------------------|
		|           ~          |          a          |
		|           i          |          e          |
		|           o          |          i          |
		|           ?          |          o          |
		|           a          |          u          |
		'----------------------'---------------------'
	[ ] Si ces charactères sont présent, vous devez les ignorer:
		.---------------------.
		| CARACTÈRE À IGNORER |
		|---------------------|
		|          >          |
		|          a          |
		|          e          |
		|          i          |
		|          o          |
		|          u          |
		'---------------------'
	[ ] Afficher le message décrypté.

Voici des exemples d’entrée et sortie valide:
[ ] "Ha-i>lilu>-?>i>o>i> W>aei>-?r>luo>d!"
	-> "Hello World!"
[ ] "C-?enig>a>ir>-~t-al-~t-o>-?nos Yao-?-a eooiodo>ii-od o-oit>u!ia Se-?
	cu-?a-?uula! Iut'oso r-ia>>u-~lly -oncro-id-oeu>>iib>l-ieeaaui tih-~t
	y>-?-aa c>i>-~n ur-i>-~uuood>au toh-~tui >>m>e-iss-~gooo-io>!"
	-> "Congratulations You did it! So cool! It's really incredible that yo
	can read that
message!"

'''

# https://realpython.com/python-main-function/
# https://www.w3schools.com/python/python_classes.asp
# https://www.datacamp.com/tutorial/python-private-methods-explained
# https://www.geeksforgeeks.org/python/protected-variable-in-python/

CHAR_TARGET	=	"~io?a"
CHAR_VALUE	=	"aeiou"
CHAR_IGNORE	=	">aeiou"

PROMPT_IN	=	"Veuillez entrer une phrase à décrypter: "

class Decrypt:
	_decrypted = ""
	_encrypted = ""
	def __init__( self ):
		self.setEncrypted()

	def setEncrypted( self ):
		user_input = ""
		while user_input == "":
			user_input = input( PROMPT_IN )
		self._encrypted = user_input

	#def _decrypt( self ):

	def getEncrypted( self ):
		print( self._encrypted )

	def getDecrypted( self ):
		print( self._decrypted )

def main():
	message = Decrypt()

if __name__ == "__main__":
	main()
