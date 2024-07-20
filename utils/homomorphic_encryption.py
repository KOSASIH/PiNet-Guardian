import numpy as np
from phe import paillier

class HomomorphicEncryption:
    def __init__(self):
        self.public_key, self.private_key = paillier.generate_paillier_keypair()

    def encrypt(self, data):
        encrypted_data =[self.public_key.encrypt(x) for x in data]
        return encrypted_data

    def decrypt(self, encrypted_data):
        decrypted_data = [self.private_key.decrypt(x) for x in encrypted_data]
        return decrypted_data

    def add_homomorphically(self, encrypted_data1, encrypted_data2):
        result = [x + y for x, y in zip(encrypted_data1, encrypted_data2)]
        return result

    def multiply_homomorphically(self, encrypted_data, scalar):
        result = [x * scalar for x in encrypted_data]
        return result
