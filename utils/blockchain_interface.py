import hashlib
from ecdsa import SigningKey, SECP256k1

class BlockchainInterface:
    def __init__(self):
        self.private_key = SigningKey.from_secret_exponent(123456789, curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()

    def generate_transaction(self, data):
        transaction = {
            "data": data,
            "timestamp": int(time.time()),
            "hash": self.generate_hash(data)
        }
        return transaction

    def generate_hash(self, data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode("utf-8"))
        return hash_object.hexdigest()

    def sign_transaction(self, transaction):
        signature = self.private_key.sign(transaction["hash"].encode("utf-8"))
        return signature

    def verify_transaction(self, transaction, signature):
        return self.public_key.verify(signature, transaction["hash"].encode("utf-8"))
