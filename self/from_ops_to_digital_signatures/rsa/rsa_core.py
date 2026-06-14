from rsa.utilities import fast_pow, generate_prime, inverse_mod


def generate_pair_keys(bit_length : int) -> tuple[tuple[int, int], tuple[int, int]]:

    p = generate_prime(bit_length // 2)
    q = generate_prime(bit_length // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    assert phi > e
    
    d = inverse_mod(e, phi)

    return (e, n), (d, n)

def rsa_transform(message : int, key : tuple[int, int]) -> int:
    assert 0 < message < key[1]
    return fast_pow(message, key[0], key[1])