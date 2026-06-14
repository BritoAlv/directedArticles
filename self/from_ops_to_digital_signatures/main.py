from random import randint

from division.division_binary_search import division_binary_search
from division.division_naive import division_naive
from division.division_school import division_school
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
    pub, priv = rsa_api.generate_keys(1024)
    encoded_message = rsa_api.encrypt(message, pub)
    decoded_message = rsa_api.decrypt(encoded_message, priv)
    print(decoded_message)
    

def main():
    rsa_main()
    
        


if __name__ == "__main__":
    main()
