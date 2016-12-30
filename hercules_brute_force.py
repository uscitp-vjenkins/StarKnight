"""
Brute Force Password Cracker
Codename : Hercules 

Vincent Jenkins 
ITP - 125 
StarKnightSecurity 

"""    
import string
import itertools
import hashlib
import timeit
original_hashes = open("hashes.txt","r")
alphabet = string.ascii_letters + string.digits + string.punctuation 
iteration = 1
while iteration <= 8:
	start_time = timeit.default_timer()
	passwords = itertools.product(alphabet, repeat= iteration)
	iteration += 1
	for hashes_original in iter(original_hashes.readline,''):
			for words in passwords:	
				hashes = hashlib.md5(''.join(words).encode()).hexdigest()
				if hashes == hashes_original.strip():
					print(''.join(words))
					elapsed = timeit.default_timer() - start_time
					print(elapsed)
			else:
				break
original_hashes.close()

