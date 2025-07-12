
# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	id: int = 0
	def __init__( self, name: str ):
		id += 1
		self._name: str = name

	def getName( self ):
		return ( self._name )

class Product:
	id: int = 0
	def __init__(	self, \
			  		name: str, \
					value: int, \
					user: User ):
		id += 1
		self._name:str = name
		self._value: int = value
		self._owner: User = user

class Computer( Product ):
	id: int = 0
	def __init__(	self, \
			  	product_name: str, \
				product_value: int, \
				product_owner: User, \
					year: int, \
					cpu_type: str, \
					gpu_type: str, \
					ram_gb: int, \
					hd_gb: int ):
		id += 1
		super().__init__( product_name, product_value, product_owner )
		self._year: int = year
		self._cpu_type: str = cpu_type
		self._gpu_type: str = gpu_type
		self._ram_gb: int = ram_gb
		self._hd_gb: int = hd_gb

class Screen( Product ):
	id: int = 0
	def __init__(	self, \
				product_name: str, \
				product_value: int, \
				product_owner: User, \
			  		display_size: int, \
					hdmi_port: bool ):
		id += 1
		super().__init__( product_name, product_value, product_owner )
		self._display_size_in: int = display_size
		self._hdmi_port: bool = hdmi_port

class Keyboard( Product ):
	id: int = 0
	types: dict[str, tuple[str:str]] = {	"100%"	: (100, "full-size"), \
						 					"80%"	: (80, "tenkeyless"), \
											"75%"	: (75, "compact"), \
											"65%"	: (65, "small"),
											"60%"	: (60, "most compact") }
	def __init__(	self, \
				product_name: str, \
				product_value: int, \
				product_owner: User, \
			  		wireless: bool, \
					mechanical: bool, \
					type: tuple[str,str] ):
		id += 1
		super().__init__( product_name, product_value, product_owner )
		self._wireless: bool = wireless
		self._mechanical: bool = mechanical
		self._type = type

class Mouse( Product ):
	id: int = 0
	def __init__(	self,
				product_name: str, \
				product_value: int, \
				product_owner: User, \
					wireless: bool, \
					button_amount: int ):
		id += 1
		super().__init__( product_name, product_value, product_owner )
		self._wireless: bool = wireless
		self._button_amount: int = button_amount

class Inventory:
	def __init__( self ):
		pass

	def list_inventory( self ):
		"""
		Format: [{Type} - {name} - {attribut} - {...}]
		"""
		pass

	def search_by_name( self, product_name: str ):
		pass

	def give_to( self, products: list[Product], recipient: User ):
		pass

	def search_by_price( self, product_price: int ):
		pass

	def search_by_monitor( self ):
		pass

	def search_by_keyboard_info( self, wireless: bool, mechanical: bool  ):
		pass

	def search_by_keyboard_type( self, type: str ):
		pass

	def search_by_mouse( self ):
		pass

	
