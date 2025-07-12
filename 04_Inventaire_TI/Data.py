# https://docs.python.org/3/library/stdtypes.html

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
					user: User = None ):
		Product.__id += 1
		self._name:str = name
		self._value: int = value
		self._owner: User = user
		self._productId = Product.__id

	def getName( self ):
		return ( self._name )

	def getPrice( self ):
		return ( self._value )

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
				product_value: int, \
				#product_owner: User, \
					year: int, \
					cpu_type: str, \
					gpu_type: str, \
					ram_gb: int, \
					hd_gb: int ):
		Computer.__id += 1
		super().__init__( product_name, product_value )
		self._year: int = year
		self._cpu_type: str = cpu_type
		self._gpu_type: str = gpu_type
		self._ram_gb: int = ram_gb
		self._hd_gb: int = hd_gb
		self._id = Computer.__id

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
				product_value: int, \
				#product_owner: User, \
			  		display_size: int, \
					hdmi_port: bool ):
		Screen.__id += 1
		super().__init__( product_name, product_value )
		self._display_size_in: int = display_size
		self._hdmi_port: bool = hdmi_port
		self._id = Screen.__id

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
				product_value: int, \
				#product_owner: User, \
			  		wireless: bool, \
					mechanical: bool, \
					type: tuple[str,str] ):
		Keyboard.__id += 1
		super().__init__( product_name, product_value )
		self._wireless: bool = wireless
		self._mechanical: bool = mechanical
		self._type = type
		self._id = Keyboard.__id

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
				product_value: int, \
				#product_owner: User, \
					wireless: bool, \
					button_amount: int ):
		Mouse.__id += 1
		super().__init__( product_name, product_value )
		self._wireless: bool = wireless
		self._button_amount: int = button_amount
		self._id = Mouse.__id

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

	def list_inventory( self ):
		"""
		Format: [{Type} - {name} - {attribut} - {...}]
		"""
		pass

	def give_to( self, products: list[Product], recipient: User ):
		pass

	def search_by_name( self, product_name: str ):
		for product_type in self._stock:
			for product in product_type:
				if product.getName() == product_name:
					return ( product )

	def search_by_price( self, product_price: int ):
		for product_type in self._stock:
			for product in product_type:
				if product.getPrice() == product_price:
					return ( product )

	def search_by_monitor( self, size: int, hdmi: bool ):
		for product_type in self._stock:
			if type( product_type[0] ).__name__ == \
				type( Screen ).__name__:
				for product in product_type:
					if product.getSize() == size \
					and product.getHdmiPort() == hdmi:
						return ( product )

	def search_by_keyboard_info( self, wireless: bool, mechanical: bool  ):
		pass

	def search_by_keyboard_type( self, type: str ):
		pass

	def search_by_mouse( self ):
		pass

