# -------------------------------------------------------------- [ RESSOURCE.S ]

# https://stackoverflow.com/questions/1535327/how-to-print-instances-of-a-class-using-print
# https://stackoverflow.com/questions/38758668/grouping-functions-by-using-classes-in-python
# https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance

# --------------------------------------------------------------- [ CONSTANT.S ]

# -------------------- Separators
SEP			= " - "
SEP2		= " :: "
SPEC_SEP	= " "
ASSOC_SYM	= '='

# -------------------- Product
VAL		= f"value{ASSOC_SYM}"
OWN		= f"owner{ASSOC_SYM}"

# -------------------- Misc
YEAR	= f"year{ASSOC_SYM}"
WI		= f"wireless{ASSOC_SYM}"

# -------------------- Computer
CPU		= f"cpu{ASSOC_SYM}"
GPU		= f"gpu{ASSOC_SYM}"
RAM		= f"memory_size{ASSOC_SYM}"
HD		= f"disk_space{ASSOC_SYM}"

# -------------------- Screen
SCRN	= f"screen_size{ASSOC_SYM}"
HDMI	= f"hdmi{ASSOC_SYM}"

# -------------------- Keyboard
KB_TYP	= f"size_type{ASSOC_SYM}"
MECH	= f"mechanical{ASSOC_SYM}"

# -------------------- Mouse
BTNS 	= f"buttons{ASSOC_SYM}"

# -------------------- Utils
STR_BOX	= ( '[', ']' )
EMPTY_BOX = " "

# ----------------------------------------------------------------- [ CLASS.ES ]

class Util:
	def __init__( self ) -> None:
		pass

	@staticmethod
	def strBox( text: str, pad: bool = True ) -> str:
		boxed = ""
		if not text and pad:
			text = EMPTY_BOX
		return ( STR_BOX[0] + text + STR_BOX[1] )

	@staticmethod
	def plural( word: str, count: int ) -> str:
		if count > 1:
			return ( word + 's' )
		return ( word )

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
		self.__name: str		= name
		self.__value: int		= value
		self.__user: User		= user
		self.__registered: bool = False

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

	def __str__( self ) -> str:
		output = ""
		value: str = VAL + Util.strBox( str( self.__value ) )
		owner: str = OWN + Util.strBox( self.getUserName() )
		output += self.__name + SPEC_SEP + value + SPEC_SEP + owner
		return ( output )

	def register( self ) -> None:
		self.__registered = True

	def checkAttributes(	self,
				   		name: str = None,
				   		value: int = None,
						user: User = None ) -> bool:
		if (( name and name != self.__name ) or
			( value and value != self.__value ) or
			( user and user.getName() != self.getUserName() )):
			return ( False )
		return ( True )

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

	def __str__( self ) -> str:
		output: str = ""
		product_specs: str = super().__str__()
		year: str = YEAR + Util.strBox( str( self.__year ) )
		cpu: str = CPU + Util.strBox( self.__cpu )
		gpu: str = GPU + Util.strBox( self.__gpu, False )
		ram: str = RAM + Util.strBox( str( self.__ram ) )
		disk_space: str = HD + Util.strBox( str( self.__hd ) )
		output += (	self.__class__.__name__ + SEP +
					product_specs + SPEC_SEP +
					year + SPEC_SEP +
					cpu + SPEC_SEP +
					gpu + SPEC_SEP +
					ram + SPEC_SEP +
					disk_space)
		return ( output )

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

	def checkComputerAttributes(	self,
									year: int = None,
									cpu: str = None,
									gpu: str = None,
									ram: int = None,
									hd: int = None ) -> bool:
		if ( ( year and year != self.__year ) or
			 ( cpu and cpu != self.__cpu ) or
			 ( gpu and gpu != self.__gpu ) or
			 ( ram and ram != self.__ram ) or
			 ( hd and hd != self.__hd ) ):
			return ( False )
		return ( True )

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
		self.__size: float		= round( screen_size, 2 )
		self.__hdmi_port: bool	= screen_hdmi_port
		Screen.__id += 1

	def __str__( self ) -> str:
		output: str = ""
		product_specs: str = super().__str__()
		size: str = SCRN + Util.strBox( str( self.__size ) )
		hdmi: str = HDMI + Util.strBox( str( self.__hdmi_port ) )
		output += (	self.__class__.__name__ + SEP +
					product_specs + SPEC_SEP +
					size + SPEC_SEP +
					hdmi)
		return ( output )

	def getSize( self ) -> float:
		return ( self.__size )

	def getHdmiPort( self ) -> bool:
		return ( self.__hdmi_port )

	def checkScreenAttributes(	self,
								size: float = None,
								hdmi: bool = None ) -> bool:
		if (( size and round(size, 2) != self.__size ) or
			( hdmi and hdmi != self.__hdmi_port ) ):
			return ( False )
		return ( True )

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

	def __str__( self ) -> str:
		output = ""
		product_specs: str = super().__str__()
		wireless: str = WI + Util.strBox( str( self.__wireless ) )
		mechanical: str = MECH + Util.strBox( str( self.__mechanical ) )
		size_type: str = KB_TYP + Util.strBox( self.__type )
		output += (	self.__class__.__name__ + SEP +
					product_specs + SPEC_SEP +
					wireless + SPEC_SEP +
					mechanical + SPEC_SEP +
					size_type)
		return ( output )

	def getWireless( self ) -> bool:
		return ( self.__wireless )

	def getMechanical( self ) -> bool:
		return ( self.__mechanical )

	def getType( self ) -> str:
		return ( self.__type )

	def checkKeyboardAttributes(	self,
									wireless: bool = None,
									mechanical: bool = None,
									kb_type: str = None ) -> bool:
		if ( ( wireless != self.__wireless ) or
	  		 ( mechanical != self.__mechanical ) or
			 ( kb_type != self.__type ) ):
			return ( False )
		return ( True )

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

	def __str__( self ) -> str:
		output:str = ""
		product_specs = super().__str__()
		wireless: str = WI + Util.strBox( str( self.__wireless ) )
		buttons: str = BTNS + Util.strBox( str( self.__button_amount ) )
		output += (	self.__class__.__name__ + SEP +
			 		product_specs + SPEC_SEP +
					wireless + SPEC_SEP +
					buttons )
		return ( output )

	def getWireless( self ) -> bool:
		return ( self.__wireless )

	def getButtonAmount( self ) -> int:
		return ( self.__button_amount )

	def checkMouseAttributes(	self,
								wireless: bool = None,
								buttons: bool = None ) -> bool:
		if ( ( wireless and wireless != self.__wireless ) or
	  		 ( buttons and buttons != self._buttons ) ):
			return ( False )
		return ( True )

class Inventory:
	def __init__( self ) -> None:
		self.__stock: list[Product] = []

	def add_product( self, product: Product ):
		self.__stock.append( product )
		product.register()

	def list_inventory( self ):
		for product in self.__stock:
			print( product )

	def list_inventory_of_user( self ):
		pass

	def list_values( self ):
		pass

	def give_to( self ):
		pass

	def __search_by_product(	self,
								name: str = None,
								value: int = None,
								user: User = None ) -> Product:
		for product in self.__stock:
			if product.checkAttributes( name, value, user ):
				return ( product )
		return ( None )

	def __search_by_monitor(	self,
								size: float = None,
								hdmi: bool = None ) -> Product:
		for product in self.__stock:
			if( isinstance( product, Screen ) and
			product.checkScreenAttributes( size, hdmi ) ):
					return ( product )
		return ( None )

	def __search_by_keyboard(	self,
								wireless: bool = None,
								mechanical: bool = None,
								kb_type: str = None ) -> Product:
		for product in self.__stock:
			if ( isinstance( product, Keyboard ) and
	   		product.checkKeyboardAttributes( wireless, mechanical, kb_type ) ):
				return ( product )
		return ( None )

	def __search_by_computer(	self,
								year: int = None,
								cpu: str = None,
								gpu: str = None,
								ram: int = None,
								hd: int = None) -> Product:
		for product in self.__stock:
			if ( isinstance( product, Computer ) and
			product.checkComputerAttributes( year, cpu, gpu, ram, hd ) ):
				return ( product )
		return ( None )

	def __search_by_mouse(	self,
							wireless: bool = None,
							buttons: bool = None ) -> Product:
		for product in self.__stock:
			if ( isinstance( product, Mouse ) and
	   		product.checkMouseAttributes( wireless, buttons ) ):
				return ( product )
		return ( None )

	def search_by_name( self, name: str ) -> Product:
		return ( self.__search_by_product( name, None, None ) )

	def search_by_price( self, value: int  ) -> Product:
		return ( self.__search_by_product( None, value, None ) )

	def search_monitor( self, size: float, hdmi: bool ):
		return ( self.__search_by_monitor( size, hdmi ) )

	def search_keyboard_info( self, wireless: bool, mechanical: bool  ):
		return ( self.__search_by_keyboard( wireless, mechanical, None ) )

	def search_keyboard_type( self, kb_type: str ):
		return ( self.__search_by_keyboard( None, None, kb_type ) )

	def search_computer( self, ram: int, hard_disk: int ):
		return ( self.__search_by_computer( None, None, None, ram, hard_disk ) )

	def search_mouse( self, wireless: bool, button_amount: bool ):
		return ( self.__search_by_mouse( wireless, button_amount ) )

	def list_quantity( self ):
		count = Computer.count()
		print(	f"Quantity of {Util.plural( "computer", count)} in " +
				f"inventory {ASSOC_SYM} {count} " )
		count = Screen.count()
		print(	f"Quantity of {Util.plural( "screen", count)} in " +
				f"inventory {ASSOC_SYM} {count} " )
		count = Keyboard.count()
		print(	f"Quantity of {Util.plural( "keyboard", count)} in " +
				f"inventory {ASSOC_SYM} {count} " )
		count = Mouse.count()
		print(	f"Quantity of {Util.plural( "mouse", count)} in " +
				f"inventory {ASSOC_SYM} {count} " )
