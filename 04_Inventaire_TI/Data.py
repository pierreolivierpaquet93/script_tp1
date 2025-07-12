
# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	def __init__( self, name: str ):
		self._name: str = name

	def getName( self ):
		return ( self._name )

class Product:
	def __init__(	self, \
			  		name: str, \
					value: int, \
					user: User ):
		self._name:str = name
		self._value: int = value
		self._owner: User = user

class Computer( Product ):
	def __init__(	self, \
			  	product_name: str, \
				product_value: int, \
				product_owner: User, \
					year: int, \
					cpu_type: str, \
					gpu_type: str, \
					ram_gb: int, \
					hd_gb: int ):
		super().__init__( product_name, product_value, product_owner )
		self._year: int = year
		self._cpu_type: str = cpu_type
		self._gpu_type: str = gpu_type
		self._ram_gb: int = ram_gb
		self._hd_gb: int = hd_gb

class Screen( Product ):
	def __init__(	self, \
				product_name: str, \
				product_value: int, \
				product_owner: User, \
			  		display_size: int, \
					hdmi_port: bool ):
		super().__init__( product_name, product_value, product_owner )
		self._display_size_in: int = display_size
		self._hdmi_port: bool = hdmi_port

class Keyboard( Product ):
	types: dict[int:tuple[int,str]] = {	100	: (100, "full-size"), \
						 				80	: (80, "tenkeyless"), \
										75	: (75, "compact"), \
										65	: (65, "small"),
										60	: (60, "most compact") }
	def __init__(	self, \
				product_name: str, \
				product_value: int, \
				product_owner: User, \
			  		wireless: bool, \
					mechanical: bool, \
					type: tuple[int,str] ):
		super().__init__( product_name, product_value, product_owner )
		self._wireless: bool = wireless
		self._mechanical: bool = mechanical
		self._type = type

class Mouse( Product ):
	def __init__(	self,
				product_name: str, \
				product_value: int, \
				product_owner: User, \
					wireless: bool, \
					button_amount: int ):
		super().__init__( product_name, product_value, product_owner )
		self._wireless: bool = wireless
		self._button_amount: int = button_amount
