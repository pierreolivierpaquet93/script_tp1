# https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters

# --------------------------------------------------------------- [ CONSTANT.S ]

CHAR_TARGETS	=	"~io?a"
CHAR_VALUES		=	"aeiou"
CHAR_IGNORE		=	">aeiou"

FLAG			=	'-'

PROMPT_IN	=	"Veuillez entrer une phrase à décrypter: "

# ----------------------------------------------------------------- [ CLASS.ES ]
# https://www.w3schools.com/python/python_classes.asp
# https://www.datacamp.com/tutorial/python-private-methods-explained
# https://www.geeksforgeeks.org/python/protected-variable-in-python/

class Decrypt:
	_decrypted = ""
	_encrypted = ""
	_size = 0

	def __init__( self, msg_to_decrypt=None ):
		if not msg_to_decrypt:
			self.setEncrypted()
		else:
			self.setEncrypted( msg_to_decrypt )

	def setEncrypted( self, msg_to_decrypt=None ):
		"""
			- Takes input from user (user_input)
			- Stores the original input.
			- Launch the decrypting method.
		"""
		if msg_to_decrypt:
			self._encrypted = msg_to_decrypt
		else:
			user_input = ""
			while user_input == "":
				user_input = input( PROMPT_IN )
			self._encrypted = user_input
		self._decrypt()

	def _decrypt( self ):
		"""
			- Parses encrypted message.
			- Searching for FLAG
				- If found, validates the following character.
			- Also validates if each character should be ignored.
		"""
		self._size = len( self._encrypted )
		i = 0
		while i < self._size:
			if self._encrypted[i] == FLAG:
				i += 1
				if i < self._size:
					l = self._checkTargetChar( self._encrypted[i] )
					if l >= 0:
						self._decrypted += ( CHAR_VALUES[l] )
			elif self._checkIgnoreChar( self._encrypted[i] ) == False:
				self._decrypted += ( self._encrypted[i] )
			i += 1
		print( self._decrypted )

	def _checkTargetChar( self, char ):
		"""
			:param str char: 
			:return: The index from CHAR_TARGETS where [char] was found. \
			Returns -1 if [char] was not found.
		"""
		i = 0
		size = len( CHAR_TARGETS )
		while i < size:
			if CHAR_TARGETS[i] == char:
				return( i )
			i += 1
		return ( -1 )

	def _checkIgnoreChar( self, char ):
		"""
			:param str char: A single character from an encrypted message.
			:return: Whether [char] was found in CHAR_IGNORE
		"""
		for letter in CHAR_IGNORE:
			if letter == char:
				return( True )
		return( False )

	def getEncrypted( self ):
		return( self._encrypted )

	def getDecrypted( self ):
		return( self._decrypted )

	def displayEncrypted( self ):
		print( self.getEncrypted() )

	def displayDecrypted( self ):
		print( self.getDecrypted() )

# --------------------------------------------------------------------- [ MAIN ]
# https://realpython.com/python-main-function/

def main():
	message = Decrypt()
	test1=Decrypt( "Yoo-i-ih!" )

if __name__ == "__main__":
	main()
