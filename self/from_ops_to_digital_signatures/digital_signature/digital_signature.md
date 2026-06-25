## Digital Signature

The problem: Implement digitally a system for transactions between a bank and its customers.

Let's say there is a bank, one of its customers tells the bank operator to send X$ to other account. After this happens, the customer denies having done the transaction, how does the bank prove to a judge that the customer is trying to scam it?

The bank ask the customer to confirm the transaction, how does the bank can receive an answer, and check it was done by the customer, this type of system needs some features:

- the bank can't use the customer signature to create faked orders.
- the custom can't deny later the confirmation of the order. ie, it should not only be authentication, also should be something that confirms that only the customer could have produced it.
- the bank should confirm that what was received, wasn't altered, from the moment the customer wrote it, accept it.

Was if can be proved that this is Alice signature, but not that Alice signed this message, basically their signature should be tied to the message itself, else this could happen.


The solution is for the bank have something that allows them to ensure that the customer was the one that gave the order, 

The order should come with something that only the customer can produce, this way the bank can prove to the judge that the customer sent the order. This thing produced by the customer should depend on the order, because if not so the bank can use this something to say that the customer sent more orders, which could be false.

Basically, to implement a digital email system, is needed a way for the receiver of an email, confirm that the assumed emitter was the one that actually sent the email.

Two things:
    - something only someone can produce
    - the something sent is only valid to the data sent.

This can be solved with the public key cryptography approach, and hash functions.

Let's say bank Y produces an order for customer X, and customer X should confirm the transaction, bank Y has a public key of its customer X, customer X encrypts the order with its private key and sent it to the bank. 

The bank uses the public key to decrypt the order, and this way the bank can assure that only customer X could have produced that order. Now this order is unique, so the bank can take that encrypted code and use it to fake orders from customer X.

Finally in practice, Public Key cryptography is not adecuated for large message, thus to avoid having to encrypt the order, a hash of it is produced with a hash function. Or a one way function without exit doors. 

The bank receives the message, decrypts it with the public key, and compares it to the hash of the order, that he can compute. 

Again in the email situation, the email data is hashed, and encrypted with the private key of the sender, thus both the email and the encrypted value is sent over the network, somehow, encrypted, 

The receiver does the decryption process and checks if the hash match, observe that this approach ensures data integrity, because else the hashes can't match.

## CIA Triad

Confidentiality: means only the intended target can read the data.

Integrity: means guaranteeing that the data received is exactly the data that was sent.

Authenticity: means that's possible to verify the identity of the sender.

Non-repudiation: means that the sender can't deny later having sent the message.

Availability: means that the data can be accessed whenever is needed

Authorization : means that determines what a user is allowed to do.

## The Integrity Problem:

When using public key cryptography, let's say I encrypt a message with the public key, and send it, when it's decrypted using the private key.

How does the receiver, i.e. the owner of the private key knows that what was decrypted is actually what was sent?

This problem is called integrity, in the sense that the direct encryption / decryption process does not guarantee that the decrypted data is what actually was sent, how deal with this?

Encrypting with the public key only provides confidentiality, which means that only I can decrypt the message. Observe that integrity does not guarantee authenticity, in the sense, that with integrity the owner of the private key, decrypts the data, and with the integrity check can determine whether this is a valid message or a corrupted one, 

But that does not prevent that someone on the middle, steals the original data, and put its own, which can pass the integrity check. To ensure authenticity is needed the digital signature approach. 

But the digital signature approach comes with non-repudiation also, a question is it possible to achieve authenticity and integrity without non-repudiation?

Why if there are digital signatures are needed a trusted third party?

Because a digital signature approach says that the owner of the private key signed the data, but that can't prove that the owner of the private key is the expected company or person.

Trusted third parties or certificate authorities do this job. Their job is to keep track of public keys, and ensure that they are related to their identities.

So www.x.com shares its public key to the trusted third party, but if I directly ask the third party for the public key of www.x.com I'm vulnerable to receive something different.

To deal with this, os, browsers come with the installed public key of the trusted third party, this way can be checked that one is actually communicating with messages signed by the trusted third party. Basically it shifts the responsibility to the browser, the OS and the trusted third party.

The other advantage of the third part is that it can revoke a specific public key from www.x.com, in case that www.x.com gets hacked, else if this is not done, the math would still working. 

Interaction between browser and site www.x.com:

 1. Browser connects to www.x.com
 2. www.x.com sends its certificate signed by the TTP, with a date. 
 3. Browser checks the digital signature using TTP public key.
 4. Browser verifies the date is recent enough to check that's not revoked.

Interaction between www.x.com and TTP:

First step is to get a certificate from the TTP, to achieve this the site has to generate a pair of public / private keys on their own server. Then submit a request to the TTP to create a certificate which includes the public key and the domain name. The TTP should certify via a challenge that this step is being realized by admins of the city www.x.com. After this, the TTP takes the public key, wraps it in a certificate and digitally signs it with its private key, which the admins of the www.x.com site receive back. But here is the catch.

Now with this certificate signed by the TTP, they send it to visitors of their webpage, and them can check it was signed by the TTP so it's fine.

Remains to explain how to deal with the issue of emergency revokation, if the private key of the site gets stolen, 

Someone can setup a fake site, and replace the original one, while the admins of the original site. 

Tell TPP to revoke the certificate, but the only way that the devices can know about this is after the certificate revocation time expires, and is needed a new one. How browsers deal with this situation?  

