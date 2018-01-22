import string 

print("1. Encrypt Text")
print("2. Encrypt File")
print("3. Decrypt Text")
print("4. Decrypt File")
select = raw_input("Selection: ")

def read_file():
	filename = raw_input("File name: ")
	file = open(filename, 'r')
	plaintext = file.read()
	file.close()
	return plaintext

def write_file(text):
	save = raw_input("\nSave to file? (Y/N): ")
	if save == 'Y':
		filename = raw_input("Output filename: ")
		file = open(filename, 'w')
		file.write(text)
		file.close()
		print("Saved!")

if select == "1" or select == "2":
	if select == "1":
		plaintext = raw_input("Input plaintext: ")
	else :
		plaintext = read_file()

	key = raw_input("Input key: ")

	key_length = len(key)
	key_char_itt = 0
	chiper_text = ''

	for c in plaintext:

		if c.isalpha():
			if key_char_itt == key_length:
				key_char_itt = 0

			plain_index = string.ascii_uppercase.index(c.upper())
			key_index = string.ascii_uppercase.index(key[key_char_itt].upper())

			key_char_itt += 1

			chip_index = (plain_index + key_index) % 26

			if c.islower():
				chiper_text += string.ascii_uppercase[chip_index].lower()
			else:
				chiper_text += string.ascii_uppercase[chip_index]
		else:
			chiper_text += c

	if select == "1":

		print("\n1. Print look alike plaintext")
		print("2. Print without whitespace")
		print("3. Print in groups of 5 letters")

		p = raw_input("Selection: ")
		print("\nPlain Text: "+plaintext)

		if p == "1":
			print("Chiper text: "+chiper_text)
			write_file(chiper_text)
		elif p == "2":
			print("Chiper text: "+chiper_text.replace(" ", ""))
			write_file(chiper_text.replace(" ",""))
		elif p == "3":
			c_temp = chiper_text.replace(" ","")
			text = ''
			groups = 0
			for c in c_temp:
				if groups == 4:
					text += ' '+c
					groups = 0
				else:
					text += c
					groups += 1
			print("Chiper text: "+text)
			write_file(text)

	else :
		write_file(chiper_text)

elif select == "3" or select == "4":
	if select == "3":
		chipertext = raw_input("Chiper Text: ")
	else:
		chipertext = read_file()

	key = raw_input("Input key: ")

	key_length = len(key)
	key_char_itt = 0
	plaintext = ''

	for c in chipertext:
		if c.isalpha():
			if key_char_itt == key_length:
				key_char_itt = 0

			chip_index = string.ascii_uppercase.index(c.upper())
			key_index = string.ascii_uppercase.index(key[key_char_itt].upper())

			key_char_itt += 1

			plain_index = (chip_index - key_index) % 26
			
			if c.islower():
				plaintext += string.ascii_uppercase[plain_index].lower()
			else:
				plaintext += string.ascii_uppercase[plain_index]
		else:
			plaintext += c

	if select == "3":
		print("\nChiper Text: "+chipertext)
		print("Plain Text: "+plaintext)
	else:
		write_file(plaintext)