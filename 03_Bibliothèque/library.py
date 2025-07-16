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

	def getTitle( self ):
		return (self._title)

class User:
	count: int = 0

	def __init__( self, username, age ):
		self._userId: int = User.count
		User.count += 1
		self._username: str = username
		self._age: int = age
		self._books: list[Book] = [] # Empty Book list.
		return

	def checkHowManyBooks( self ):
		qt = self.getBooksQuantity()
		print(	f"I {self.getUsername()} currently have " +
				f"{qt} {conjugate("book", qt)}." )
		return

	def borrowBook( self, book_to_borrow: Book ):
		self._books.append( book_to_borrow )
		return

	def getBooksQuantity( self ) -> int:
		return ( len( self._books ) )

	def getUsername( self ) -> str:
		return ( self._username )

	def returnBooks(	self,
						library_books: list[Book],
						titles:list[str] = None ):
		if titles == None: # Return all books
			for book in self._books:
				library_books.append( book )
			self._books.clear() # Removes all the book from the list.
		else:
			for title in titles:
				for book in self._books:
					if book.getTitle() == title:
						self._books.remove( book )
						break
		return

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
			print(	f"The {self.getName()} library currently have " +
		 			f"{count} {conjugate("book", count)} of genre {genre}" )

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

	def returnAllBook( self, user:User ):
		user.returnBooks( self._books, None )
		return

# ------------------------------------------------------------------- [ TOOL.S ]

def conjugate( word:str, amount:int ) -> str:
	if amount > 1 and word[len(word)-1] != 's':
		return ( word + 's' )
	return ( word )

# --------------------------------------------------------------------- [ MAIN ]

def main():
	books = [
		Book("To Kill a Mockingbird", "Fiction"),Book("1984", "Dystopian"),
		Book("The Great Gatsby", "Fiction"),
		Book("Harry Potter and the Sorcerer's Stone", "Fantasy"),
		Book("The Hobbit", "Fantasy"),
		Book("Pride and Prejudice", "Romance"),
		Book("The Catcher in the Rye", "Fiction"),
		Book("The Lord of the Rings", "Fantasy"),
		Book("Brave New World", "Dystopian"),
		Book("Jane Eyre", "Romance"),
		Book("Fahrenheit 451", "Dystopian"),
		Book("The Chronicles of Narnia", "Fantasy"),
		Book("Moby Dick", "Fiction"),
		Book("Wuthering Heights", "Romance"),
		Book("The Da Vinci Code", "Thriller"),
		Book("The Girl with the Dragon Tattoo", "Thriller"),
		Book("Gone Girl", "Thriller"),
		Book("The Hunger Games", "Dystopian"),
		]

	library = Library("Limoilou", books)

	jacob = User("Jacob", 18)
	martine = User("Martine", 26)
	richard = User("Richard", 42)

	library.tryBorrowBookOfType(jacob, "Fantasy")
	library.tryBorrowBookOfType(jacob, "Fantasy")
	library.tryBorrowBookOfType(jacob, "Fantasy")
	library.tryBorrowBookOfType(jacob, "Fantasy")
	library.tryBorrowBookOfType(richard, "Fantasy")
	library.tryBorrowBookOfType(richard, "Fantasy")
	library.tryBorrowBookOfType(richard, "Romance")
	library.tryBorrowBookOfType(martine, "Dystopian")
	library.tryBorrowBookOfType(martine, "Dystopian")
	library.tryBorrowBookOfType(martine, "Dystopian")

	jacob.checkHowManyBooks()
	martine.checkHowManyBooks()
	richard.checkHowManyBooks()
	library.checkAllBookByGenre()

	library.returnAllBook(jacob)
	jacob.checkHowManyBooks()
	martine.checkHowManyBooks()
	richard.checkHowManyBooks()
	library.checkAllBookByGenre()

if __name__ == "__main__":
	main()
