# -------------------------------------------------------------- [ RESSOURCE.S ]


# --------------------------------------------------------------- [ CONSTANT.S ]

SEP		= " - "
SEP2	= " :: "

# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	def __init__(	self,
					name: str,
					id = 0 ) -> None:
		self.__name: str = name
		self.__id: int = id

	def getName( self ) -> str:
		return ( self.__name )

	def getId( self ) -> int:
		return ( self.__id )

class Product:
	def __init__(	self,
			  		name: str,
					value: int,
					user: User = None ) -> None:
		self.__name: str	= name
		self.__value: int	= value
		self.__user: User	= user

	def getName( self ) -> str:
		return ( self.__name )

	def getValue( self ) -> int:
		return ( self.__value )

	def getUser( self ) -> User:
		return ( self.__User )

	def getUserName( self ) -> str:
		if self.__user:
			return ( self.__user.getName() )

	def setUser( self, new_user: User ) -> None:
		if not self.__user:
			self.__user = new_user
			return ( True )
		return ( False )

class Computer ( Product ):
	__id: int = 0

	@staticmethod
	def count() -> int:
		return ( Computer.__id )

	def __init__(	self,
					product_name: str,
					computer_year: int,
					computer_cpu: str,
					computer_gpu: str,
					computer_ram: int,
					computer_hd: int,
					product_value: int,
					product_user: User = None) -> None:
		super().__init__( product_name, product_value, product_user )
		self.__year: int	= computer_year
		self.__cpu: str		= computer_cpu
		self.__gpu: str		= computer_gpu
		self.__ram: int		= computer_ram
		self.__hd: int		= computer_hd
		Computer.__id += 1

	def getYear( self ) -> int:
		return ( self.__year )

	def getCpu( self ) -> str:
		return ( self.__cpu )

	def getGpu( self ) -> str:
		return ( self.__gpu )

	def getRam( self ) -> int:
		return ( self.__ram )

	def getHd( self ) -> int:
		return ( self.__hd )

class Screen ( Product ):
	__id: int = 0

	@staticmethod
	def count() -> int:
		return ( Screen.__id )

	def __init__(	self,
					product_name: str,
					screen_size: float,
					screen_hdmi_port: bool,
					product_value: int,
					product_user: User = None ) -> None:
		super().__init__( product_name, product_value, product_user )
		self.__size: float		= screen_size
		self.__hdmi_port: bool	= screen_hdmi_port
		Screen.__id += 1

	def getSize( self ) -> float:
		return ( self.__size )

	def getHdmiPort( self ) -> bool:
		return ( self.__hdmi_port )

class Keyboard ( Product ):
	__id: int = 0

	@staticmethod
	def count() -> int:
		return ( Keyboard.__id )

	def __init__(	self,
					product_name: str,
					keyboard_wireless: bool,
					keyboard_mechanical: bool,
					keyboard_type: str,
					product_value: int,
					product_user: User = None ) -> None:
		super().__init__( product_name, product_value, product_user )
		self.__wireless: bool	= keyboard_wireless
		self.__mechanical: bool	= keyboard_mechanical
		self.__type: str		= keyboard_type
		Keyboard.__id += 1

	def getWireless( self ) -> bool:
		return ( self.__wireless )

	def getMechanical( self ) -> bool:
		return ( self.__mechanical )

	def getType( self ) -> str:
		return ( self.__type )

class Mouse ( Product ):
	__id: int = 0

	@staticmethod
	def count() -> int:
		return ( Mouse.__id )

	def __init__(	self,
					product_name: str,
					mouse_wireless: bool,
					mouse_button_amount: int,
					product_value: int,
					product_user: User = None ) -> None:
		super().__init__( product_name, product_value, product_user )
		self.__wireless: bool		= mouse_wireless
		self.__button_amount: int	= mouse_button_amount
		Mouse.__id += 1

	def getWireless( self ) -> bool:
		return ( self.__wireless )

	def getButtonAmount( self ) -> int:
		return ( self.__button_amount )

class Inventory:
	def __init__( self ):
		self.__stock: Product = []

	def add_product( self ):
		pass

	def list_inventory( self ):
		pass

	def list_inventory_of_user( self ):
		pass

	def list_values( self ):
		pass

	def give_to( self ):
		pass

	def search_by_name( self ):
		pass

	def search_by_price( self ):
		pass

	def search_monitor( self ):
		pass

	def search_keyboard_info( self ):
		pass

	def search_keyboard_type( self ):
		pass

	def search_computer( self ):
		pass

	def list_quantity( self ):
		pass
