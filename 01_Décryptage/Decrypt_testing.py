import decrypt

GRN = "\033[1;32m"
RED = "\033[1;31m"
RST = "\033[0m"

SEPARATOR = "-----------------------------------------"

TEST_AMOUNT = 5
TEST_OK = f"{GRN}[ OK ]{RST}"
TEST_KO = f"{RED}[ KO ]{RST}"

TEST	=	f"{SEPARATOR*2}\nTest "
TEST_1	=	f"{TEST}#1\n",\
			"Ha-i>lilu>-?>i>o>i> W>aei>-?r>luo>d!",\
			"Hello World!"
TEST_2	=	f"{TEST}#2\n",\
			"C-?enig>a>ir>-~t-al-~t-o>-?nos Yao-?-a eooiodo>ii-od o-oit>u!ia" +\
			" Se-? cu-?a-?uula! Iut'oso r-ia>>u-~lly -oncro-id-oeu>>iib>l-ie" +\
			"eaaui tih-~t y>-?-aa c>i>-~n ur-i>-~uuood>au toh-~tui >>m>e-iss" +\
			"-~gooo-io>!",\
			"Congratulations You did it! So cool! It's really incredible tha" +\
			"t you can read that message!"
TEST_3	=	f"{TEST}#3\n",\
			"-",\
			""
TEST_4	=	f"{TEST}#4\n",\
			">>>aeiou>>>",\
			""
TEST_5	=	f"{TEST}#5\n",\
			"-~-i-o-?-a",\
			f"{decrypt.CHAR_VALUES}"
# -------------------------------------------------------------------- [ TESTS ]

print( f"{TEST_1[0]}" + f"Encrypted: {TEST_1[1]}" )
message = decrypt.Decrypt( TEST_1[1] )
if message.getDecrypted() == TEST_1[2]:
	print( TEST_OK )
else:
	print( TEST_KO )

print( f"{TEST_2[0]}" + f"Encrypted: {TEST_2[1]}" )
message = decrypt.Decrypt( TEST_2[1] )
if message.getDecrypted() == TEST_2[2]:
	print( TEST_OK )
else:
	print( TEST_KO )

print( f"{TEST_3[0]}" + f"Encrypted: {TEST_3[1]}" )
message = decrypt.Decrypt( TEST_3[1] )
if message.getDecrypted() == TEST_3[2]:
	print( TEST_OK )
else:
	print( TEST_KO )

print( f"{TEST_4[0]}" + f"Encrypted: {TEST_4[1]}" )
message = decrypt.Decrypt( TEST_4[1] )
if message.getDecrypted() == TEST_4[2]:
	print( TEST_OK )
else:
	print( TEST_KO )

print( f"{TEST_5[0]}" + f"Encrypted: {TEST_5[1]}" )
message = decrypt.Decrypt( TEST_5[1] )
if message.getDecrypted() == TEST_5[2]:
	print( TEST_OK )
else:
	print( TEST_KO )
