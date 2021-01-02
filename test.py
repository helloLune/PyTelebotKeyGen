from utils import keygen, log

def checkup_len():
	log('generating key with len from 0 to 50')
	for l in range(51):
		key = keygen(l)
		log('len of key is', len(key))
		log(
			f'len(key) equals {l}, test passed' if len(
				key
			) == l else f'len(key) doesn\'t equals {l}, test failed'
		)

checkup_len()