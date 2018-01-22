def write_file(text):
	save = raw_input("\nSave to file? (Y/N): ")
	if save == 'Y':
		filename = raw_input("Output filename: ")
		file = open(filename, 'w')
		file.write(text)
		file.close()
		print("Saved!")

alpha = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

print("1. Encrypt Text")
print("2. Decrypt Text")
select = raw_input("Selection: ")

plaintext = raw_input("Input plaintext: ")
key = raw_input("Input key: ")
uniq_chars = ''

for c in key:
	if c not in uniq_chars and c != ' ' and c != 'J':
		uniq_chars += c

for c in alpha:
	if c not in uniq_chars:
		uniq_chars += c

key = [] 
col = []
col_index = 0
i = 0
first_char = ''

while i < len(uniq_chars):

	if col_index < 5:
		if col_index == 0:
			first_char = uniq_chars[i]

		col.append(uniq_chars[i])
		col_index += 1
		i += 1
	else:
		col.append(first_char)
		key.append(col)
		col = []
		col_index = 0

col.append(first_char)
key.append(col)
key.append(key[0])

# chunking plaintext
groups = []
group = ''
i = 0

while i < len(plaintext):
	if plaintext[i] != ' ':
		if plaintext[i] not in group:
			group += plaintext[i]
			i += 1
		else:
			group += 'Z'

		if len(group) == 2:
			groups.append(group)
			group = ''
	else:
		i+=1

if len(group) == 1:
	groups.append(group+'Z')

cipher = []
for group in groups:
	row = 0
	i = 0

	while i < 5:
		if group[0] in key[i]:

			row = i
			break
		i += 1


	# same row
	if group[1] in key[row]:
		char_chunk = ''
		for c in group:
			if select == "1":
				char_chunk += key[row][key[row].index(c)+1]
			elif select == "2":
				if key[row].index(c) == 0:
					i = 1
					col = 0
					while i < len(key[row]):
						if key[row][i] == c:
							col = i
						i += 1
					char_chunk += key[row][col-1]
					continue

				char_chunk += key[row][key[row].index(c)-1]


		cipher.append(char_chunk)
		continue


	i = 0
	col = 0
	found = False

	while i < 5:
		if group[1] == key[row][i]:
			col = i
			found = True
			break
		i+= 1

	# same column
	if found:
		char_chunk = ''
		for c in group:
			# if select == "2":
			char_chunk += key[key[row].index(c)+1][col]

		cipher.append(char_chunk)

	else: 
	# character chunk not in same row or column
		col = []
		row = []

		for c in group:
			i = 0
			while i < 5:
				j = 0
				while j < 5:
					if c == key[i][j]:
						col.append(i)
						row.append(j)
						break
					j += 1
				i+=1
		cipher.append(key[col[0]][row[1]]+key[col[1]][row[0]])
if select == "1":
	print("\nPlain text: "+plaintext)

	text = ''
	for group in cipher:
		text += group + ' '

	print("cipher text: "+text)
	write_file(text)
	
elif select == "2":
	plain = ''
	i = 0
	while i < len(cipher):
		if 'Z' in cipher[i]:
			if i < len(cipher) - 1:
				if cipher[i][0] == cipher[i+1][0]:
					plain += cipher[i][0]
				else:
					plain += cipher[i]
			else :
				plain += cipher[i]
		else:
			plain += cipher[i]
		i += 1

	print(plain)