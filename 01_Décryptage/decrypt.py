# -------------------------------------------------------------- [ RESSOURCE.S ]

# https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters

# ----------------------------------------------------------------- [ MODULE.S ]

# TESTING
# https://cs.stanford.edu/people/nick/py/python-main.html
import sys

# --------------------------------------------------------------- [ CONSTANT.S ]

#COLORS
ESC	= "\033["
BLU	= f"{ESC}" + "1;34m"
RST	= f"{ESC}" + "0m"

CHAR_TARGETS	= "~io?a"
CHAR_VALUES		= "aeiou"
CHAR_IGNORE		= ">aeiou"

FLAG	= '-'

PROMPT_IN	= f"{BLU}Veuillez entrer une phrase à décrypter: {RST}"

# ----------------------------------------------------------------- [ CLASS.ES ]
# https://www.w3schools.com/python/python_classes.asp
# https://www.datacamp.com/tutorial/python-private-methods-explained
# https://www.geeksforgeeks.org/python/protected-variable-in-python/

class Decrypt:
	def __init__( self, msg_to_decrypt: str = None ):
		self.__decrypted: str = ""
		self._encrypted: str = ""
		self._size: int = 0
		if not msg_to_decrypt:
			self.setEncrypted()
		else:
			self.setEncrypted( msg_to_decrypt )

	def setEncrypted( self, msg_to_decrypt: str = None ):
		"""
		- If needed (no string provided), takes input from user (user_input)
		- Stores the encrypted (original) input.
		- Launch the decrypting method.
		"""
		if msg_to_decrypt:
			self._encrypted = msg_to_decrypt
		else:
			user_input = ""
			while user_input == "":
				user_input = input( PROMPT_IN )
			self._encrypted = user_input
		self._size = len( self._encrypted )
		self.__decrypt()

	def __decrypt( self ):
		"""
		- Parses encrypted message.
		- Searching for FLAG
			- If found, validates the following character.
		- Also validates if each character should be ignored.
		"""
		i = 0
		char_tmp = ""
		while i < self._size:
			char_tmp = self._encrypted[i]
			if char_tmp == FLAG:
				i += 1
				if i < self._size:
					# next: using self._encrypted[i] because it's only used once
					l = self.__checkTargetChar( self._encrypted[i] )
					if l >= 0:
						self.__decrypted += ( CHAR_VALUES[l] )
			elif self.__checkIgnoreChar( char_tmp ) == False:
				self.__decrypted += ( char_tmp )
			i += 1
		print( self.__decrypted )

	def __checkTargetChar( self, char ) -> int:
		"""
		Parameters
		.
		- char -> Sought character
		Returns
		.
		- The index from CHAR_TARGETS constant where [char] was found.
		- OR -1 if [char] was not found.
		"""
		i = 0
		size = len( CHAR_TARGETS )
		while i < size:
			if CHAR_TARGETS[i] == char:
				return ( i )
			i += 1
		return ( -1 )

	def __checkIgnoreChar( self, char ) -> bool:
		"""
		Parameters
		.
		- char -> A single character from an encrypted message.
		Returns
		.
		Whether [char] was found in CHAR_IGNORE constant.
		"""
		for letter in CHAR_IGNORE:
			if letter == char:
				return( True )
		return ( False )

	def getEncrypted( self ) -> str:
		return ( self._encrypted )

	def getDecrypted( self ) -> str:
		return ( self.__decrypted )

	def displayEncrypted( self ):
		print( self.getEncrypted() )

	def displayDecrypted( self ):
		print( self.getDecrypted() )

# --------------------------------------------------------------------- [ MAIN ]
# https://realpython.com/python-main-function/

def main() -> int:
	arguments = sys.argv

	if len( arguments ) > 1:
		message = Decrypt( arguments[1] )
	else:
		message = Decrypt()
	return ( 0 )

if __name__ == "__main__":
	main()
