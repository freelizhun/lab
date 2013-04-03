from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import os
from datetime import datetime
from re import sub
import time
import hashlib
# AES is a block cipher so you need to define size of block.
# Valid options are 16, 24, and 32




class encData(object):
    def __init__(self):

        self.BLOCK_SIZE = 32

        self.INTERRUPT = u'\u0001'
        self.PAD = u'\u0000'

        #message='test'
        #filename= hashlib.sha256(message).hexdigest()

        self.IV = u'12345678abcdefgh'

        #self.SECRET_KEY=self.filename[0:32]

    def AddPadding(self, data, interrupt, pad, block_size):
        new_data = ''.join([data, interrupt])
        new_data_len = len(new_data)
        remaining_len = block_size - new_data_len
        to_pad_len = remaining_len % block_size
        pad_string = pad * to_pad_len
        return ''.join([new_data, pad_string])


    def StripPadding(self, data, interrupt, pad):
        return data.rstrip(pad).rstrip(interrupt)


    def EncryptWithAES(self, encrypt_cipher, plaintext_data):
        plaintext_padded = self.AddPadding(plaintext_data, self.INTERRUPT, self.PAD, self.BLOCK_SIZE)
        encrypted = encrypt_cipher.encrypt(plaintext_padded)
        return encrypted
#return b64encode(encrypted)


    def DecryptWithAES(self, decrypt_cipher, encrypted_data):
        #decoded_encrypted_data = b64decode(encrypted_data)
        decrypted_data = decrypt_cipher.decrypt(encrypted_data)
        return self.StripPadding(decrypted_data, self.INTERRUPT, self.PAD)

    def encrypt(self, our_data_to_encrypt, filename):
        SECRET_KEY=filename[0:32]
        cipher_for_encryption = AES.new(SECRET_KEY, AES.MODE_CBC, self.IV)
        encrypted_data = self.EncryptWithAES(cipher_for_encryption, our_data_to_encrypt)
        return encrypted_data


    def decrypt(self, encrypted_data, filename):
        SECRET_KEY=filename[0:32]
        cipher_for_decryption = AES.new(SECRET_KEY, AES.MODE_CBC, self.IV)
        decrypted_data = self.DecryptWithAES(cipher_for_decryption, encrypted_data)
        return decrypted_data

   

