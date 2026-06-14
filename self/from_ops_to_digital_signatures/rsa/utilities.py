import random
import string 
from primality import primality
from gcd.euclid import extended_euclid


def fast_pow(x: int, e: int, mod: int) -> int:
    if e == 0:
        return 1
    if e == 1:
        return x
    result = fast_pow(x, e // 2, mod)
    result *= result
    result %= mod
    if e % 2 == 1:
        result *= x
        result %= mod
    return result


def inverse_mod(x: int, mod: int) -> int:
    _, a, _ = extended_euclid(x, mod)
    return a % mod


def generate_prime(bit_length: int) -> int:
    while True:
        prime_candidate = random.randint(1 << (bit_length - 1), (1 << (bit_length)) - 1)
        if is_prime(prime_candidate):
            return prime_candidate


def is_prime(candidate: int) -> bool:
    return primality.isprime(candidate)

def decode_key(key: str) -> tuple[int, int]:
    d, n = key.split(",")
    return (int(d), int(n))


def encode_key(key: tuple[int, int]) -> str:
    return f"{key[0]},{key[1]}"

s = string.printable
base = len(s)

def encode_message(message: str) -> int:
    number = 0
    for i in range(len(message)):
        number *= base
        letter = message[i]
        index = s.find(letter)
        assert 0 <= index < len(s)
        number += index
    return number



def decode_message(message: int) -> str:
    message_str = ""
    while message > 0:
        next = message % base
        message_str = s[next] + message_str
        message = message // base
    return message_str 
