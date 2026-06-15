from random import randint

from digital_signature.digital_signature import DigitalSignature
from basic_operations.division_binary_search import division_binary_search
from basic_operations.division_naive import division_naive
from basic_operations.division_school import division_school
from gcd import coprime_experiment
from rsa import rsa_api


def division_main():
    divisions = [division_naive, division_binary_search, division_school]
    for _ in range(10):
        a, b = randint(1, 10), randint(1, 10)
        for division in divisions:
            print(division(a, b), end=" ")
        print()


def rsa_main():
    message = "Hello World"
    pub, priv = rsa_api.generate_keys(128)
    encoded_message = rsa_api.encrypt(message, pub)
    decoded_message = rsa_api.decrypt(encoded_message, priv)
    print(decoded_message)


def digital_signature_main():
    message = "Hello World"
    digital_signature = DigitalSignature(1024)
    signed_message = digital_signature.sign(message)

    public_key = digital_signature.public_key
    print(DigitalSignature.check_signed_data(message, signed_message, public_key))


def main():
    coprime_experiment.experiment(100000, 100000)


if __name__ == "__main__":
    main()
