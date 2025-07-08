
"""
● Créer un programme en Python
	○ Ne pas utiliser de librairie externe
● Créer une classe nommée Book
	○ Contient un nom de livre (reçu en création)
	○ Contient un genre de livre (reçu en création)
● Créer une classe nommée User
	○ Contient un nom d'utilisateur (reçu en création)
	○ Contient un âge d'utilisateur (reçu en création)
	○ Contient un userId
	○ Contient une liste de livre emprunté (vide par défaut)
	○ Fonction: checkHowManyBooks
		■ Dois afficher le nom de l'utilisateur, ainsi que le nombre de livres
empruntés
	○ NOTE: Ne peut pas emprunter plus de 3 livres en même temps
● Créer une classe nommée Library
	○ Contient un nom de bibliotheque (reçu en création)
	○ Contient une liste de livre (reçu en création)
	○ Fonction: tryBorrowBookOfType
		■ Paramètre #1 User
		■ Paramètre #2 str (Genre du livre)
		■ Va vérifier s'il y a un livre du genre disponible et le donner à l'utilisateur
(s'il peut emprunter le livre)
	○ Function: checkAllBookByGenre
		■ Dois afficher le nom de la bibliothèque ainsi que la quantité de livres de
chaque genre de livre encore dans la bibliothèque
"""

# --------------------------------------------------------------- [ CONSTANT.S ]

MAX_BORROWED_BOOKS_QUANTITY	= 3

# ----------------------------------------------------------------- [ CLASS.ES ]
# https://www.tutorialspoint.com/how-to-count-the-number-of-instances-of-a-class-in-python
# https://stackoverflow.com/questions/1924469/define-a-list-with-type

class Book:
	def __init__( self, title, genre ):
		self._title = title
		self._genre = genre

	def getGenre( self ):
		return (self._genre)

class User:
	count: int = 0

	def __init__( self, username, age ):
		self._userId: int = User.count
		User.count += 1
		self._username: str = username
		self._age: int = age
		self._books: list[Book] = [] # Empty Book list.

	def checkHowManyBooks( self ):
		print( f"I {self.getUsername()} currently have " + \
				f"{self.getBooksQuantity()} book(s)." )

	def borrowBook( self, book_to_borrow: Book ):
			self._books.append( book_to_borrow )

	def getBooksQuantity( self ):
		return ( len( self._books ) )

	def getUsername( self ):
		return ( self._username )

class Library:
	def __init__( self, library_name, books: list[Book] ):
		self._name = library_name
		self._books: list[Book] = books

	def tryBorrowBookOfType( self, user: User, genre: str):
		if user.getBooksQuantity() > MAX_BORROWED_BOOKS_QUANTITY:
			return
		for book in self._books:
			if book.getGenre() == genre:
				user.borrowBook( book )
				self._books.remove( book )

# --------------------------------------------------------------------- [ MAIN ]

def main():
	user1 = User( "Toto", 42 )
	books: list[Book] = [ Book( "Harry Potter", "Magie" ),\
					  	Book( "Bible", "Religion" ), \
						Book( "Bescherelle", "Langue" ) ]
	library = Library( "Bibliotheque", books )
	library.tryBorrowBookOfType( user1, "Religion" )

if __name__ == "__main__":
	main()
