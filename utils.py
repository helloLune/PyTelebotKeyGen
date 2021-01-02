from random import randint
from string import printable

def keygen(n):
	pattern = printable[:62] # numbers & letters
	pattern_len = len(pattern)
	random_char = lambda _: pattern[randint(0, pattern_len-1)]
	return ''.join(map(random_char, range(n)))

def log(*args):
	print('>', *args)