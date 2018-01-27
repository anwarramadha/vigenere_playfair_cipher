import string 

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

extended_ascii = [chr(i) for i in xrange(256)]

print("1. Encrypt Text")
print("2. Encrypt File")
print("3. Decrypt Text")
print("4. Decrypt File")
select = raw_input("Selection: ")

inp = ''
if select == "1" or select == "3":
	print("\n1. Input from keyboard")
	print("2. Input from text file")
	inp = raw_input("Selection: ")

if select == "1" or select == "2":
	if inp == "1":
		plaintext = raw_input("Input plaintext: ")
	else :
		plaintext = read_file()

	key = raw_input("Input key: ")

	key_length = len(key)
	key_char_itt = 0
	cipher_text = ''

	for c in plaintext:

		if c in extended_ascii:
			if key_char_itt == key_length:
				key_char_itt = 0

			plain_index = extended_ascii.index(c)
			key_index = extended_ascii.index(key[key_char_itt])

			key_char_itt += 1

			chip_index = (plain_index + key_index) % len(extended_ascii)

			cipher_text += extended_ascii[chip_index]
		else:
			cipher_text += c

	if select == "1":
		print("\nPlain Text: "+plaintext)

		print("Like plaintext: "+cipher_text)

		c_temp = cipher_text.replace(" ","")
		print("Without whitespace: "+c_temp)

		text = ''
		groups = 0
		for c in c_temp:
			if groups == 4:
				text += ' '+c
				groups = 0
			else:
				text += c
				groups += 1
		print("In 5 letters: "+text)
		write_file(cipher_text)

	else :
		write_file(cipher_text)

elif select == "3" or select == "4":
	if inp == "1":
		ciphertext = raw_input("cipher Text: ")
	else:
		ciphertext = read_file()

	key = raw_input("Input key: ")

	key_length = len(key)
	key_char_itt = 0
	plaintext = ''

	for c in ciphertext:
		if c in extended_ascii:
			if key_char_itt == key_length:
				key_char_itt = 0

			chip_index = extended_ascii.index(c)
			key_index = extended_ascii.index(key[key_char_itt])

			key_char_itt += 1

			plain_index = (chip_index - key_index) % len(extended_ascii)
			
			plaintext += extended_ascii[plain_index]
		else:
			plaintext += c

	if select == "3":
		print("\ncipher Text: "+ciphertext)
		print("Plain Text: "+plaintext)
	else:
		write_file(plaintext)