import hashlib

from rsa import rsa_api



class DigitalSignature:
    def __init__(self, bits=1024):
        self.bits = bits
        self.private_key, self.public_key = rsa_api.generate_keys(self.bits)

    def sign(self, message: str) -> str:
        hashed_message = DigitalSignature.hash_message(message)
        signed_message = rsa_api.encrypt(hashed_message, self.private_key)
        return signed_message
    

    @staticmethod
    def hash_message(message: str) -> str:
        hash = hashlib.sha256(message.encode())
        hash_hex = hash.hexdigest()
        return hash_hex

    @staticmethod
    def check_signed_data(message: str, signed_message: str, public_key: str) -> bool:
        hashed_message = DigitalSignature.hash_message(message)
        decrypted_message = rsa_api.decrypt(signed_message, public_key)
        return hashed_message == decrypted_message