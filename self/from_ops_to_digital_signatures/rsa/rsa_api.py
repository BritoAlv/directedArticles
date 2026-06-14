from rsa import rsa_core
from rsa.utilities import decode_key, decode_message, encode_key, encode_message


def generate_keys(bit_length: int) -> tuple[str, str]:
    public, private = rsa_core.generate_pair_keys(bit_length)
    return encode_key(public), encode_key(private)

def _transform(message : str, key : str) -> str:
    decoded_key = decode_key(key)
    message_int = encode_message(message)
    encrypted_message = rsa_core.rsa_transform(message_int, decoded_key)
    return decode_message(encrypted_message)


def encrypt(message: str, public_key: str) -> str:
    return _transform(message, public_key)


def decrypt(message: str, private_key: str) -> str:
    return _transform(message, private_key)