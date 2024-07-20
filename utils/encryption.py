import hashlib
import base64

class Encryption:
    def __init__(self):
        self.hash_algorithm = hashlib.sha256

    def encrypt_data(self, data):
        encrypted_data = self.hash_algorithm.update(data.encode("utf-8")).digest()
        return base64.b64encode(encrypted_data)

    def decrypt_data(self, encrypted_data):
        decrypted_data = base64.b64decode(encrypted_data)
        return decrypted_data.decode("utf-8")
