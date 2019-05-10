import base64
from Crypto.Cipher import AES
from Crypto import Random
import sys, os
key = 'd3adb33f13371337'
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

class AESCipher:

    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def main():
    if len(sys.argv) != 2:
        exit(1)
    in_file = sys.argv[1]
    if os.path.isfile(in_file):
        out_file = in_file + '.enc'
        fin = file(in_file, 'rb').read()
        fout = file(out_file, 'wb')
        cypher = AESCipher(key)
        enc_data = cypher.encrypt(fin)
        fout.write(enc_data)
        fout.close()


if __name__ == '__main__':
    main()

