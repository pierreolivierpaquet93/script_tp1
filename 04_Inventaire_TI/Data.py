# https://docs.python.org/3/library/stdtypes.html

# --------------------------------------------------------------- [ CONSTANT.S ]

SEP	= " - "

# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	"""
	Class variable.s
	.
	- __id -> Total amount of User.

	Instance variable.s
	.
	- _name -> User's name.
	- _id -> User.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( User.__id )

	def __init__( self, name: str ):
		User.__id += 1
		self._name: str = name
		self._id = User.__id

	def getName( self ):
		return ( self._name )

class Product:
	"""
	Class variable.s
	.
	- __id -> Total amount of Product.

	Instance variable.s
	.
	- _name -> Product's name.
	- _value -> Product's price/value ($).
	- _owner -> User who owns the Product. None by default.
	- _productId -> Product.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( Product.__id )

	def __init__(	self, \
			  		name: str, \
					value: int, \
					user: User, \
					track: bool):
		if track == True:
			Product.__id += 1
			self._productId = Product.__id
		else:
			self._productId = -1
		self._name: str = name
		self._value: int = value
		self._owner: User = user

	def getName( self ):
		return ( self._name )

	def getPrice( self ):
		return ( self._value )

	def getOwner( self ):
		if self._owner != None:
			return self._owner.getName()
		return ( "" )

	def setOwner( self, new_owner: User ):
		if self._owner == None:
			self._owner = new_owner
			return ( new_owner )
		return ( None )

class Computer( Product ):
	"""
	Parent
	.
	Product

	Class variable.s
	.
	- __id -> Total amount of Computer.

	Instance variable.s
	.
	- _year -> Year when the Computer was bought.
	- _cpu_type -> ex: "i7-14700".
	- _gpu_type -> ex: "RTX 4060 Ti".
	- _ram_gb -> Amount of RAM in GigaBytes.
	- _hd_gp -> Amount of storage (Hard Disk) in GigaBytes.
	- _id -> Computer.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( Computer.__id )

	def __init__(	self, \
			  	product_name: str, \
					year: int, \
					cpu_type: str, \
					gpu_type: str, \
					ram_gb: int, \
					hd_gb: int,
				product_value: int, \
				product_owner: User = None, \
					track: bool = True):
		if track == True:
			Computer.__id += 1
			self._id = Computer.__id
		else:
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._year: int = year
		self._cpu_type: str = cpu_type
		self._gpu_type: str = gpu_type
		self._ram_gb: int = ram_gb
		self._hd_gb: int = hd_gb

	def getYear( self ):
		return ( self._year )

	def getCpu( self ):
		return ( self._cpu_type )

	def getGpu( self ):
		return ( self._gpu_type )

	def getRam( self ):
		return ( self._ram_gb )

	def getHardDisk( self ):
		return ( self._hd_gb )

class Screen( Product ):
	"""
	Parent
	.
	Product

	Class variable.s
	.
	- __id -> Total amount of Screen.

	Instance variable.s
	.
	- _display_size_in -> Screen size in inches (in).
	- _hdmi_port -> Whether there is an HDMI port.
	- _id -> Screen.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( Screen.__id )

	def __init__(	self, \
				product_name: str, \
			  		display_size: int, \
					hdmi_port: bool, \
				product_value: int, \
				product_owner: User = None,
					track: bool = True ):
		if track == True:
			Screen.__id += 1
			self._id = Screen.__id
		else:
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._display_size_in: int = display_size
		self._hdmi_port: bool = hdmi_port

	def getSize( self ):
		return ( self._display_size_in )

	def getHdmiPort( self ):
		return ( self._hdmi_port )

class Keyboard( Product ):
	"""
	Parent
	.
	Product

	Class variable.s
	.
	- __id -> Total amount of Keyboard.
	- types -> Dictionnary of standard Keyboard types. ex: Keyboard.types["65%"]

	Instance variable.s
	.
	- _wireless -> Whether the Keyboard is wireless.
	- _mechanical -> Whether the Keyboard is mechanical.
	- _type: tuple[str:str] -> ("percentage", "description")
	- _id -> Keyboard.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( Keyboard.__id )

	types: dict[str, tuple[str:str]] = {	"100%"	: (100, "full-size"), \
						 					"80%"	: (80, "tenkeyless"), \
											"75%"	: (75, "compact"), \
											"65%"	: (65, "small"),
											"60%"	: (60, "most compact") }

	def __init__(	self, \
				product_name: str, \
			  		wireless: bool, \
					mechanical: bool, \
					kb_type: str, \
				product_value: int, \
				product_owner: User = None, \
					track: bool = True ):
		if track == True:
			Keyboard.__id += 1
			self._id = Keyboard.__id
		else:
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._wireless: bool = wireless
		self._mechanical: bool = mechanical
		if kb_type != "":
			self._type = Keyboard.types[kb_type]

	def getWireless( self ):
		return ( self._wireless )

	def getMechanical( self ):
		return ( self._mechanical )

	def getType( self ):
		return ( str( self._type[0] ) + '%' )

class Mouse( Product ):
	"""
	Parent
	.
	Product

	Class variable.s
	.
	- __id -> Total amount of Mouse.

	Instance variable.s
	.
	- _wireless -> Whether the Mouse is wireless.
	- _button_amount -> Quantity of Mouse buttons.
	- _id -> Mouse.__id when instance was constructed.
	"""
	__id: int = 0

	def count():
		return ( Mouse.__id )

	def __init__(	self,
				product_name: str, \
					wireless: bool, \
					button_amount: int,
				product_value: int, \
				product_owner: User = None, \
					track: bool = True ):
		if track == True:
			Mouse.__id += 1
			self._id = Mouse.__id
		else:
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._wireless: bool = wireless
		self._button_amount: int = button_amount

	def getWireless( self ):
		return ( self._wireless )

	def getButtonAmount( self ):
		return ( self._button_amount )

class Inventory:
	"""
	Instance variable.s
	.
	- _stock -> List of Product lists.
	"""
	def __init__( self ):
		self._stock: list[list[Product]] = []
		pass

	def add_product( self, product:Product ):
		for product_type in self._stock: # Itering throught Product lists.
			if type( product_type[0] ).__name__ == type( product ).__name__:
				product_type.append( product ) # Adds product to its list.
				return
		new_list = []
		new_list.append( product )
		self._stock.append( new_list )
		return

	def __list_inventory_computer( self, computer: Computer ) -> str:
		output = ""
		output += "year=[" + str( computer.getYear() ) + "] "
		output += "cpu=[" + computer.getCpu() + "] "
		output += "gpu=[" + computer.getGpu() + "] "
		output += "memory_size=[" + str( computer.getRam() ) + "] "
		output += "disk_space=[" + str( computer.getHardDisk() ) + "]"
		return ( output )

	def __list_inventory_screen( self, screen: Screen ) -> str:
		output = ""
		output += "screen_size=[" + str( screen.getSize() ) + "] "
		output += "hdmi=[" + str( screen.getHdmiPort() ) + "]"
		return ( output )

	def __list_inventory_keyboard( self, keyboard: Keyboard ) -> str:
		output = ""
		output += "wireless=[" + str( keyboard.getWireless() ) + "] "
		output += "mechanical=[" + str( keyboard.getMechanical() ) + "] "
		output += "size_type=[" + keyboard.getType() + "] "
		return ( output )

	def __list_inventory_mouse( self, mouse: Mouse ):
		output = ""
		output += "wireless=[" + str( mouse.getWireless() ) + "] "
		output += "buttons=[" + str( mouse.getButtonAmount() ) + "]"
		return ( output )

	def list_inventory( self ):
		funcs = {	type( Computer( "",0,"","",0,0,0,None,0 ) ).__name__: \
		   				self.__list_inventory_computer,
		  			type( Screen( "",0,0,0,None,0 ) ).__name__ : \
						self.__list_inventory_screen,
					type( Keyboard("",0,0,"",None, None, 0) ).__name__ : \
						self.__list_inventory_keyboard,
					type( Mouse("",0,0,0,None,0) ).__name__ : \
						self.__list_inventory_mouse }
		for product_type in self._stock:
			for product in product_type:
				output: str = ""
				output += type( product_type[0] ).__name__
				output += SEP + product.getName() + " "
				output += "value=[" + str( product.getPrice() ) + "] "
				owner: str = product.getOwner()
				if owner == "":
					owner += " "
				output += f"owner=[" + owner + "] "
				product_function = funcs[ type( product ).__name__ ]
				output += product_function( product )
				print( output )


	def give_to( self, products: list[Product], recipient: User ):
		for product in products:
			if product != None:
				if product.getOwner() == "":
					product.setOwner( recipient )

	def search_by_name( self, product_name: str ):
		for product_type in self._stock:
			for product in product_type:
				if product.getName() == product_name:
					return ( product )
		return ( None )

	def search_by_price( self, product_price: int ):
		for product_type in self._stock:
			for product in product_type:
				if product.getPrice() == product_price:
					return ( product )
		return ( None )

	def search_by_monitor( self, size: int, hdmi: bool ):
		screen_tmp = Screen( "",0,0, False,None,False )
		for product_type in self._stock:
			if product_type != None and type( product_type[0] ).__name__ == \
				type( screen_tmp ).__name__:
				for product in product_type:
					if product.getSize() == size \
					and product.getHdmiPort() == hdmi:
						return ( product )
		return ( None )

	def search_by_keyboard_info( self, wireless: bool, mechanical: bool  ):
		keyboard_tmp = Keyboard( "", 0, False, False, ("",""),None,False)
		for product_type in self._stock:
			if product_type != None and type( product_type[0] ).__name__ == \
				type( keyboard_tmp ).__name__:
				for product in product_type:
					if product.getWireless() == wireless \
					and product.getMechanical() == mechanical:
						return ( product )
		return ( None )

	def search_by_keyboard_type( self, keyboard_type: str ):
		keyboard_tmp = Keyboard( "", 0, False, False, ("",""),None,False)
		for product_type in self._stock:
			if product_type != None and type( product_type[0] ).__name__ == \
				type( keyboard_tmp ).__name__:
					for product in product_type:
						if product.getType() == keyboard_type:
							return ( product )
		return ( None )

	def search_by_mouse( self, wireless: bool, button_amount: int ):
		mouse_tmp = Mouse( "", 0, False, 0, None, False )
		for product_type in self._stock:
			if product_type != None and type( product_type[0] ).__name__ == \
				type( mouse_tmp ).__name__:
					for product in product_type:
						if product.getWireless() == wireless \
						and product.getButtonAmount() == button_amount:
							return ( product )
		return ( None )

	def list_quantity( self ):
		print( f"Quantity of computer(s) in inventory = {Computer.count()}" )
		print( f"Quantity of screen(s) in inventory = {Screen.count()}" )
		print( f"Quantity of keyboard(s) in inventory = {Keyboard.count()}" )
		print( f"Quantity of mouse(s) in inventory = {Mouse.count()}" )

