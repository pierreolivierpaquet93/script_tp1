
# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	def __init__( self, name: str ):
		self._name = name

	def getName( self ):
		return ( self._name )

class Product:
	def __init__(	self, \
			  		name: str, \
					value: int, \
					user: User ):
		self._name:str = name
		self._value:int = value
		self._owner = user

class Computer( Product ):
	def __init__(	self, \
			  		product_name: str, \
					product_value: int, \
					product_user: User, \
					year: int, \
					cpu_type: str, \
					gpu_type: str, \
					ram_gb: int, \
					hd_gb: int ):
		self._year = year
		self._cpu_type = cpu_type
		self._gpu_type = gpu_type
		self._ram_gb = ram_gb
		self._hd_gb = hd_gb
		super().__init__( product_name, product_value, product_user )
