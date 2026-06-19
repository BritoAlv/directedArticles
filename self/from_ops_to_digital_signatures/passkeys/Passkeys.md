# Passkeys

A passkey is a contract between an account system and a password account manager with the following design.

A = some site that allows using passkeys.

PM = your password manager.

Let's say site A allows you to setup a passkey, to do this, you look for your password manager PM and tell to site A to do a contract with PM.

It will work on the following way, the responsibility of determining whether is you who is trying to log in, now goes fully to the PM.

If via X where X could be fingerprint, pin, sms, etc, PM determines you are you, then it should tell to the website that everything is okay, remains to explain how they agree to do this.

Using public-key cryptography, PM generate a pair of public-private keys, public key goes to the website, private key remains on PM, thus once PM determines you are you. 

It uses your private key to generate a signed message that the website can check with the private key. 

Passkeys are a way of passwordless authentication.