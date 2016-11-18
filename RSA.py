import random
def is_prime(n):
	n = int(n)
	i = n-1
	while i > 1:
		if n % i == 0:
			break
		i -= 1
	if i > 1:
		return False
	else:
		return True

def gcd(a, b):
	while a != 0 and b != 0:
		if a>b:
			a %= b
		else:
			b %= a
	return (a+b)

def multipcative_inverse(a, b):
	_div = []
	i = 0
	k = a
	c = a % b
	_div.append(int(a/b))
	while c != 0:

		i += 1
		#print(i)
		
		a = b
		#print("a=", a)
		b = c
		#print("b=", b)
		_div.append(int(a / b))
		c = a % b
	x = 0
	y = 1
	for j in range(0, i):
		#print(_div[i - 1 -j])
		n = x
		x = y
		#print(x)
		y = n - x * _div[i - 1 - j]
		#print(y)
	d = y % k
	return d


      	  
def generate_keypair(p,q):
	p = int(p)
	q = int(q)
	if not (is_prime(p) and is_prime(q)):
		raise ValueError('Both numbers must be prime.')
	elif p == q:
		raise ValurError('p and q cannot be equal')

	# n =pq	
	n = p*q
	phi = (p-1)*(q-1)
	e = random.randrange(1, phi)

	g = gcd(e, phi)
	while g != 1:
		e = random.randrange(1, phi)
		g = gcd(e, phi)

	d = multipcative_inverse(phi, e)

	return ((e, n), (d, n))	



def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
