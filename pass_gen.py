import random
import string

def random_pass_gen(stringLength=10):
	pass_char= string.ascii_letters+string.digits+string.punctuation
	return ''.join(random.choice(pass_char) for i in range(stringLength))
print("Password: ",random_pass_gen())



