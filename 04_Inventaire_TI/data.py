# -------------------------------------------------------------- [ RESSOURCE.S ]

# https://docs.python.org/3/library/stdtypes.html
# https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
# https://text-compare.com/
# https://www.pythonmorsels.com/breaking-long-lines-code-python/

# --------------------------------------------------------------- [ CONSTANT.S ]

SEP		= " - "
SEP2	= " :: "

# ----------------------------------------------------------------- [ CLASS.ES ]

class User:
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked User (User.__id).
		"""
		return ( User.__id )

	def __init__( self, name: str ):
		"""
		Parameters
		.
		- name -> Name of the User.
		"""
		User.__id += 1
		self._name: str = name
		self._id = User.__id
		return

	def getName( self ) -> str:
		return ( self._name )

class Product:
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked Product (Product.__id).
		"""
		return ( Product.__id )

	def __init__(	self,
			  		name: str,
					value: int,
					owner: User = None,
					track: bool = True ):
		"""
		Parameters
		.
		- name -> Name of the Product.
		- value -> Total value of the Product ($).
		- user -> Product owner; None by default.
		- track -> Whether the instance will be tracked; True by default.
		"""
		if track == True:
			Product.__id += 1
			self._productId = Product.__id
		else: # Product is constructed for temporary purposes.
			self._productId = -1
		self._name: str = name
		self._value: int = value
		self._owner: User = owner
		return

	def getName( self ) -> str:
		return ( self._name )

	def getPrice( self ) -> int:
		return ( self._value )

	def getOwner( self ) -> str:
		if self._owner != None:
			return self._owner.getName()
		return ( "" )

	def setOwner( self, new_owner: User ) -> User:
		if self._owner == None:
			self._owner = new_owner
			return ( new_owner )
		return ( None )

	def getId( self ) -> int:
		return ( self._productId )

class Computer( Product ):
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked Computer (Computer.__id).
		"""
		return ( Computer.__id )

	def __init__(	self,
			  	product_name: str,
					year: int,
					cpu_type: str,
					gpu_type: str,
					ram_gb: int,
					hd_gb: int,
				product_value: int,
				product_owner: User = None,
					track: bool = True):
		"""
		Parameters
		.
		- product_name -> Name of the Computer.
		- year -> Year when the Computer was bought.
		- cpu_type -> Name of the CPU; ex: "i7-14700".
		- gpu_type -> Name of the GPU; ex: "RTX 4060 Ti".
		- ram_gb -> Amount of RAM in GigaBytes.
		- hd_gp -> Amount of storage (Hard Disk) in GigaBytes.
		- product_value -> Total value of the Computer ($).
		- product_owner -> Computer owner; None by default.
		- track -> Whether the instance will be tracked; True by default.
		"""
		if track == True:
			Computer.__id += 1
			self._id = Computer.__id
		else: # Computer is constructed for temporary purposes.
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._year: int = year
		self._cpu_type: str = cpu_type
		self._gpu_type: str = gpu_type
		self._ram_gb: int = ram_gb
		self._hd_gb: int = hd_gb
		return

	def getYear( self ) -> int:
		return ( self._year )

	def getCpu( self ) -> str:
		return ( self._cpu_type )

	def getGpu( self ) -> str:
		return ( self._gpu_type )

	def getRam( self ) -> int:
		return ( self._ram_gb )

	def getHardDisk( self ) -> int:
		return ( self._hd_gb )

class Screen( Product ):
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked Screen (Screen.__id).
		"""
		return ( Screen.__id )

	def __init__(	self,
				product_name: str,
			  		display_size: int,
					hdmi_port: bool,
				product_value: int,
				product_owner: User = None,
					track: bool = True ):
		"""
		Parameters
		.
		- product_name -> Name of the Screen.
		- display_size -> Screen size in inches (in).
		- hdmi_port -> Whether there is an HDMI port.
		- product_value -> Total value of the Screen ($).
		- product_owner -> Screen owner; None by default.
		- track -> Whether the instance will be tracked; True by default.
		"""
		if track == True:
			Screen.__id += 1
			self._id = Screen.__id
		else: # Screen is constructed for temporary purposes.
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._display_size_in: int = display_size
		self._hdmi_port: bool = hdmi_port

	def getSize( self ) -> int:
		return ( self._display_size_in )

	def getHdmiPort( self ) -> bool:
		return ( self._hdmi_port )

class Keyboard( Product ):
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked Keyboard (Keyboard.__id).
		"""
		return ( Keyboard.__id )

	# Class dictionnary that contains standard keyboard layouts
	types: dict[str, tuple[str:str]] = {	"100%"	: (100, "full-size"),
						 					"80%"	: (80, "tenkeyless"),
											"75%"	: (75, "compact"),
											"65%"	: (65, "small"),
											"60%"	: (60, "most compact") }

	def __init__(	self,
				product_name: str,
			  		wireless: bool,
					mechanical: bool,
					kb_type: str,
				product_value: int,
				product_owner: User = None,
					track: bool = True ):
		"""
		Parameters
		.
		- product_name -> Name of the Keyboard.
		- wireless -> Whether the Keyboard is wireless.
		- mechanical -> Whether the Keyboard is mechanical.
		- kb_type -> Key value that is used to retrieve the right keyboard type
		from the class' dictionnary.
		- product_value -> Total value of the Keyboard ($).
		- product_owner -> Keyboard owner; None by default.
		- track -> Whether the instance will be tracked; True by default.
		"""
		if track == True:
			Keyboard.__id += 1
			self._id = Keyboard.__id
		else: # Keyboard is constructed for temporary purposes.
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._wireless: bool = wireless
		self._mechanical: bool = mechanical
		if kb_type != "":
			self._type = Keyboard.types[kb_type]

	def getWireless( self ) -> bool:
		return ( self._wireless )

	def getMechanical( self ) -> bool:
		return ( self._mechanical )

	def getType( self ) -> str:
		return ( str( self._type[0] ) + '%' )

class Mouse( Product ):
	__id: int = 0

	def count() -> int:
		"""
		Class function
		.
		Returns
		.
		The total amount of tracked Mouse (Mouse.__id).
		"""
		return ( Mouse.__id )

	def __init__(	self,
				product_name: str,
					wireless: bool,
					button_amount: int,
				product_value: int,
				product_owner: User = None,
					track: bool = True ):
		"""
		Parameters
		.
		- product_name -> Name of the Mouse.
		- wireless -> Whether the Mouse is wireless.
		- button_amount -> Quantity of Mouse buttons.
		- product_value -> Total value of the Mouse ($).
		- product_owner -> Mouse owner; None by default.
		- track -> Whether the instance will be tracked; True by default.
		"""
		if track == True:
			Mouse.__id += 1
			self._id = Mouse.__id
		else: # Mouse is constructed for temporary purposes.
			self._id = -1
		super().__init__( product_name, product_value, product_owner, track )
		self._wireless: bool = wireless
		self._button_amount: int = button_amount
		return

	def getWireless( self ) -> bool:
		return ( self._wireless )

	def getButtonAmount( self ) -> bool:
		return ( self._button_amount )

class Inventory:
	def __init__( self ):
		# Creates an empty list.
		# The main list can contain multiples lists of Product.
		self._stock: list[list[Product]] = []
		return

	def add_product( self, product:Product ):
		"""
		- Iterates throught the Product main list.
		- Compares the type of the provided product with the type of the first
		element of the pointed list.
		- When the types match, the product is added to the list.
		"""
		for product_type in self._stock: # Itering throught Product lists.
			if type( product_type[0] ).__name__ == type( product ).__name__:
				product_type.append( product ) # Adds product to its list.
				return
		new_list = []
		new_list.append( product )
		self._stock.append( new_list )
		return

	def __list_inventory_computer( self, computer: Computer ) -> str:
		"""
		Builds a string with the computer's attributes.
		"""
		output = ""
		output += "year=[" + str( computer.getYear() ) + "] "
		output += "cpu=[" + computer.getCpu() + "] "
		output += "gpu=[" + computer.getGpu() + "] "
		output += "memory_size=[" + str( computer.getRam() ) + "] "
		output += "disk_space=[" + str( computer.getHardDisk() ) + "]"
		return ( output )

	def __list_inventory_screen( self, screen: Screen ) -> str:
		"""
		Builds a string with the screen's attributes.
		"""
		output = ""
		output += "screen_size=[" + str( screen.getSize() ) + "] "
		output += "hdmi=[" + str( screen.getHdmiPort() ) + "]"
		return ( output )

	def __list_inventory_keyboard( self, keyboard: Keyboard ) -> str:
		"""
		Builds a string with the keyboard's attributes.
		"""
		output = ""
		output += "wireless=[" + str( keyboard.getWireless() ) + "] "
		output += "mechanical=[" + str( keyboard.getMechanical() ) + "] "
		output += "size_type=[" + keyboard.getType() + "]"
		return ( output )

	def __list_inventory_mouse( self, mouse: Mouse ) -> str:
		"""
		Builds a string with the mouse's attributes.
		"""
		output = ""
		output += "wireless=[" + str( mouse.getWireless() ) + "] "
		output += "buttons=[" + str( mouse.getButtonAmount() ) + "]"
		return ( output )

	def list_inventory( self, user: User = None ):
		"""
		- Creates 'funcs', a list functions uesd to extend the output based on
		the different Product types.
		- Builds the main part of Product details output.
		"""
		# Ex: funcs = { 'Computer': __list_inventory_computer(), ... }
		funcs = {	type( Computer( "",0,"","",0,0,0,None,0 ) ).__name__:
		   				self.__list_inventory_computer,
		  			type( Screen( "",0,0,0,None,0 ) ).__name__ :
						self.__list_inventory_screen,
					type( Keyboard( "",0,0,"",0,None,0 ) ).__name__ :
						self.__list_inventory_keyboard,
					type( Mouse("",0,0,0,None,0) ).__name__ :
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
				product_function = funcs[type( product ).__name__]
				output += product_function( product )
				if user == None:
					print( output )
				elif ( product.getOwner() == user.getName() ):
					print( output )
		return

	def list_inventory_of_user( self, user: User ):
		"""
		Calls for list_inventory() provididing a specific User.
		"""
		self.list_inventory( user )
		return

	def list_values( self ):
		"""
		- For each type of Product in the main inventory list (self._stock),
		calculates the totals and displays the information on the standard
		output.
		- Also adds them up to calculate the whole inventory total.
		"""
		total = 0
		for product_type in self._stock:
			total_value = 0
			if product_type != None:
				plural = ""
				if len( product_type ) > 1:
					plural = 's'
				type_tmp = type( product_type[0] ).__name__
				type_tmp = type_tmp.lower()
				for item in product_type:
					total_value += item.getPrice()
				print(	f"Value of {type_tmp}{plural} in inventory = " +
		  				f"{total_value} $" )
				total += total_value
		print( f"Total value = {total} $" )
		return

	def __locate_item( self, item_to_locate: Product ) -> bool:
		"""
		Uses the Product identification to validate whether it was previously
		added to the inventory.
		"""
		for product_type in self._stock:
			if ( product_type != None and
	   	type( item_to_locate ).__name__ == type( product_type[0] ).__name__ ):
				for item in product_type:
					if item.getId() == item_to_locate.getId():
						return ( True ) # item_to_locate is in the inventory.
		print(	f"give_to{SEP2}invalid{SEP2}product " +
				f"' {item_to_locate.getName()} ' is not in inventory, Skipped" )
		return ( False ) # item_to_locate was not found in the inventory.

	def give_to( self, products: list[Product], recipient: User ):
		"""
		Used to mark a Product as owned by adding the User to the Product data.
		"""
		for product in products:
			if product != None:
				if self.__locate_item( product ) == True:
					if product.getOwner() == "":
						product.setOwner( recipient )
					else:
						print(	f"give_to{SEP2}invalid{SEP2}product already" +
								f" assigned to someone else " +
								f"' {product.getName()} ', Skipped" )
			else:
				print( f"give_to{SEP2}invalid{SEP2}product is None, Skipped" )
		return

	def search_by_name( self, product_name: str ) -> Product:
		"""
		Used to retrieve a Product by its name.
		"""
		for product_type in self._stock:
			for product in product_type:
				if product.getName() == product_name:
					return ( product )
		print(	f"search_by_name{SEP2}no result found for name " +
				f"' {product_name} '" )
		return ( None )

	def search_by_price( self, product_price: int ) -> Product:
		"""
		Used to retrieve a Product by its price.
		"""
		for product_type in self._stock:
			for product in product_type:
				if product.getPrice() == product_price:
					return ( product )
		print(	f"search_by_price{SEP2}no result found for price " +
				f"{product_price}" )
		return ( None )

	def search_monitor(	self,
						size: int,
						hdmi: bool ) -> Product:
		"""
		Used to retrieve a Screen based on its display size and
		HDMI port presence.
		"""
		screen_tmp = Screen( "",0,0, False,None,False )
		for product_type in self._stock:
			if ( product_type != None and
		type( product_type[0] ).__name__ == type( screen_tmp ).__name__ ):
				for product in product_type:
					if ( product.getSize() == size
					and product.getHdmiPort() == hdmi ):
						return ( product )
		print(	f"search_monitor{SEP2}no result found for size ' {size} ' " +
				f"and hdmi ' {hdmi} '" )
		return ( None )

	def search_keyboard_info(	self,
								wireless: bool,
								mechanical: bool ) -> Product:
		"""
		Used to retrieve a Keyboard based on its wireless and
		mechanical attributes.
		"""
		keyboard_tmp = Keyboard( "",0,0,"",0,None,0 )
		for product_type in self._stock:
			if ( product_type != None and
			type( product_type[0] ).__name__ == type( keyboard_tmp ).__name__ ):
				for product in product_type:
					if ( product.getWireless() == wireless
					and product.getMechanical() == mechanical ):
						return ( product )
		print(	f"search_keyboard_info{SEP2}no result found for wireless " +
				f"' {wireless} ' and mechanical ' {mechanical} '" )
		return ( None )

	def search_keyboard_type( self, keyboard_type: str ) -> Product:
		"""
		Used to retrieve a Keyboard by its type (ex: '65%').
		"""
		keyboard_tmp = Keyboard( "",0,0,"",0,None,0 )
		for product_type in self._stock:
			if ( product_type != None and
			type( product_type[0] ).__name__ == type( keyboard_tmp ).__name__ ):
					for product in product_type:
						if product.getType() == keyboard_type:
							return ( product )
		print(	f"search_keyboard_type{SEP2}no result found for type " +
				f"' {keyboard_type} '" )
		return ( None )

	def search_mouse(	self,
						wireless: bool,
						button_amount: int ) -> Product:
		"""
		Used to retrieve a Mouse based on its wireless attribute and button
		amount.
		"""
		mouse_tmp = Mouse( "", 0, False, 0, None, False )
		for product_type in self._stock:
			if ( product_type != None and
			type( product_type[0] ).__name__ == type( mouse_tmp ).__name__ ):
					for product in product_type:
						if ( product.getWireless() == wireless
						and product.getButtonAmount() == button_amount ):
							return ( product )
		print(	f"search_mouse{SEP2}no result found for wireless " +
				f"' {wireless} ' and button(s) ' {button_amount} '" )
		return ( None )

	def search_computer( self, ram: int, hard_disk: int ) -> Product:
		"""
		Used to retrieve a Computer based on its RAM and Hard disk capacities.
		"""
		computer_tmp = Computer( "",0,"","",0,0,0,None,0 )
		for product_type in self._stock:
			if ( product_type != None and
			type( product_type[0] ).__name__ == type( computer_tmp ).__name__ ):
				for computer in product_type:
					if ( computer.getRam() == ram and 
					computer.getHardDisk() == hard_disk ):
						return ( computer )
		print(	f"search_computer{SEP2}no result found for memory size " +
				f"' {ram} ' and disk space ' {hard_disk} '" )
		return ( None )

	def list_quantity( self ):
		"""
		Calls each of the Product derived class' count() function to get
		the total amount of instances (tracked) / Quantity of each Product.
		"""
		count = Computer.count()
		print(	f"Quantity of computer{Inventory.__plural_tool(count)} " +
				f"in inventory = {count}" )
		count = Screen.count()
		print(	f"Quantity of screen{Inventory.__plural_tool(count)} " +
				f"in inventory = {count}" )
		count = Keyboard.count()
		print(	f"Quantity of keyboard{Inventory.__plural_tool(count)} " +
				f"in inventory = {count}" )
		count = Mouse.count()
		print(	f"Quantity of mouse{Inventory.__plural_tool(count)} " +
				f"in inventory = {count}" )
		return

	def __plural_tool( qt: int ) -> str:
		"""
		Tool function to manage the plurality of some output messages.
		"""
		if qt > 1:
			return ( 's' )
		else:
			return ( '' )
