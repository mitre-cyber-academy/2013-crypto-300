import random
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Encrypt a file using a key.')
    parser.add_argument('seed', help='The seed of the PRNG', type=int)
    parser.add_argument('plainFile', help='The file to encrypt',
        type=argparse.FileType('rb'))
    parser.add_argument('cryFile', help='The encrypted file', nargs='?',
        default='cryptFile')
    args = parser.parse_args()

    random.seed(args.seed)

    outFile = open(args.cryFile, 'wb')

    while True:
        currByte = args.plainFile.read(1)
        if(currByte == ''):
            break
        byteVal = ord(currByte)
        randVal = random.getrandbits(8)
        outFile.write(chr(byteVal ^ randVal))
    outFile.close()
    args.plainFile.close()

if __name__ == '__main__':
    main()
