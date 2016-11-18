def encrypt_caesar(plaintext, shift):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """

    #plaintext.lower()
    if shift == '':
        return plaintext
    else:
        shiftn = ord(shift) - ord("0") #Численное значение сдвига
    z = ord("z") #Численное значение буквы z
    Z = ord("Z")
    ciphertext = ""
    for i in range(0, len(plaintext)):
    	if ord(plaintext[i]) in range (65, 91):
    		if ord(plaintext[i]) + shiftn > Z:
    			ciphertext += chr(ord(plaintext[i]) - Z + ord("A") - 1 + shiftn)
    		else:
    			ciphertext += chr(ord(plaintext[i]) + shiftn)
    	else:
    	    if ord(plaintext[i]) + shiftn > z:
    	    	ciphertext += chr(ord(plaintext[i]) - z + ord("a") - 1 + shiftn)
                #print(shiftn)
    	    else:
    	    	ciphertext += chr(ord(plaintext[i]) + shiftn)	
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    if shift == '':
        return ciphertext
    else:
        shiftn = ord(shift) - ord("0") #Численное значение сдвига
    #z = ord("z") #Численное значение буквы z
    #A = ord("A")
    plaintext = ""
    for i in range(0, len(ciphertext)):
    	if ord(ciphertext[i]) in range (65, 91):
    		if ord(ciphertext[i]) - shiftn < ord("A") :
    			plaintext += chr(ord("Z") - (shiftn - (ord(ciphertext[i]) - ord("A"))) + 1 )
    		else:
    			plaintext += chr(ord(ciphertext[i]) - shiftn)
    	else:
    		#print ("zxcv")
    		if ord(ciphertext[i]) - shiftn < ord("a"):
    			plaintext += chr(ord("z") - (shiftn - (ord(ciphertext[i]) - ord("a"))) + 1 )
    		else:
    			plaintext += chr(ord(ciphertext[i]) - shiftn)
    return plaintext
ciphertext = input("input: ")
shift = input("shift: ")
print ("Зашифрованный: ", encrypt_caesar(ciphertext, shift))

ciphertext = input("input: ")
shift = input("shift: ")
print ("Расшифрованный: ", decrypt_caesar(ciphertext, shift))	    

