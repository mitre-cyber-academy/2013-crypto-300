import random
import argparse

def main():
	parser = argparse.ArgumentParser(
		description='Decrypt a file using a key.')
	parser.add_argument('seed', help='The seed of the PRNG', type=int)
	parser.add_argument('cryptFile', help='The file to decrypt',
		type=argparse.FileType('rb'))
	parser.add_argument('plainFile', help='The decrypted file', nargs='?',
		default='outFile')
	args = parser.parse_args()

	random.seed(args.seed)

	outFile = open(args.plainFile, 'wb')

	while True:
		currByte = args.cryptFile.read(1)
		if(currByte == ''):
			break
		byteVal = ord(currByte)
		randVal = random.getrandbits(8)
		outFile.write(chr(byteVal ^ randVal))
	outFile.close()
	args.cryptFile.close()

if __name__ == '__main__':
	main()
