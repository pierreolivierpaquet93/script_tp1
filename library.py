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
		if user.getBooksQuantity() >= MAX_BORROWED_BOOKS_QUANTITY:
			return
		for book in self._books:
			if book.getGenre() == genre:
				user.borrowBook( book )
				self._books.remove( book )
				break

	def checkAllBookByGenre( self ):
		genres: list[str] = self.getGenres()
		for genre in genres:
			count = 0
			for book in self._books:
				if book.getGenre() == genre:
					count += 1
			print( f"The {self.getName()} library currently have " + \
		 			f"{count} book(s) of genre {genre}" )

	def getGenres( self ) -> list[str]:
		genres: list[str] = [] # List of different genres in the library
		for book in self._books: # iterates through all the library's books
			genre_tmp = book.getGenre() # genre of the current book
			if len( genres ) == 0:
				genres.append( genre_tmp )
			else:
				is_monitored = False
				for genre in genres:
					if genre == genre_tmp:
						is_monitored = True
				if is_monitored == False:
					genres.append( genre_tmp )
		return ( genres )

	def getName( self ):
		return self._name

# --------------------------------------------------------------------- [ MAIN ]

def main():
	user1 = User( "Toto", 42 )
	books: list[Book] = [ Book( "Harry Potter", "Magie" ),\
					  	Book( "Bible", "Religion" ), \
						Book( "Bescherelle", "Langue" ), \
						Book( "Larousse", "Dictionnaire" ), \
						Book( "Persy Jackson", "Magie" ), \
						Book( "Internaute", "Dictionnaire" ) ]
	library = Library( "Bibliotheque", books )
	library.checkAllBookByGenre()
	library.tryBorrowBookOfType( user1, "Magie" )
	library.checkAllBookByGenre()

if __name__ == "__main__":
	main()
