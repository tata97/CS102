def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE
    j = 0 #маркер
    k = 0
    i = 0
    ciphertext = ""
    #keyword = keyword.lower()
    #print (keyword)


    while j != len(plaintext):
        for i in range(0,len(keyword)):
            if j == len(plaintext):
                return ciphertext
                break

            if ord(plaintext[k]) in range (65, 91):
                shiftn = ord(keyword[i]) - ord("A")
                if ord(plaintext[k]) + shiftn > ord("Z"):
                    ciphertext += chr(ord(plaintext[k]) - ord("Z") + ord("A") - 1 + shiftn)
                else:
                    ciphertext += chr(ord(plaintext[k]) + shiftn)
            else:
                shiftn = ord(keyword[i]) - ord("a")
                if ord(plaintext[k]) + shiftn > ord("z"):
                    ciphertext += chr(ord(plaintext[k]) - ord("z") + ord("a") - 1 + shiftn)
                else:
                    ciphertext += chr(ord(plaintext[k]) + shiftn)
            j += 1
            k += 1
        i = 0    
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE
    j = 0 #маркер
    k = 0
    i = 0
    plaintext = ""
    #keyword = keyword.lower()
    #print (keyword)


    while j != len(ciphertext):
        for i in range(0,len(keyword)):
            if j == len(ciphertext):
                return plaintext
                break

            if ord(ciphertext[k]) in range (65, 91):
            	shiftn = ord(keyword[i]) - ord("A")
            	if ord(ciphertext[k]) - shiftn < ord("A") :
            		plaintext += chr(ord("Z") - (shiftn - (ord(ciphertext[k]) - ord("A"))) + 1 )
            	else:
            		plaintext += chr(ord(ciphertext[k]) - shiftn)
            else:
            	shiftn = ord(keyword[i]) - ord("a")
            	if ord(ciphertext[k]) - shiftn < ord("a"):
            		plaintext += chr(ord("z") - (shiftn - (ord(ciphertext[k]) - ord("a"))) + 1 )
            	else:
            		plaintext += chr(ord(ciphertext[k]) - shiftn)
            j += 1
            k += 1
        i = 0		
    return plaintext

ciphertext = input("input: ")  
keyword = input("keyword: ")
print ("Зашифрованный текст: ", encrypt_vigenere(ciphertext,keyword))  

ciphertext = input("input: ")  
keyword = input("keyword: ")
print ("Расшифрованный текст: ", decrypt_vigenere(ciphertext,keyword))