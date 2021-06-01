print("A: Encrypt your text using Caser method")
print("B: Decrypt your Caser Encrypted text")
option = input("Choose your option? (A/B)")
s = ""
encrypt_list = []
decrypt_list = []
try:
	if(option == 'A' or option == 'a'):
		plain_text = input("Enter Plain-text/Original-text here:")
		key = int(input("Enter Encryption key here: "))
		for i in plain_text:
			x = ord(i) + key
			encrypt_list.append(chr(x))
		x_str = ''.join(encrypt_list)
		print(x_str)

	elif(option == 'B' or option == 'b'):
		cipher_text = input("Enter cipher-text/encrypted-text here:")
		key = int(input("Enter Decryption key here: "))
		for i in cipher_text:
			x = ord(i) - key
			decrypt_list.append(chr(x))
		
		y_str = ''.join(decrypt_list)
		print(y_str)

except Exception as e:
	print("Something is wrong here, please start again from begining.")