RSA
======

Demonstrates the basic functionality of the Riverst - Shamir - Adleman cryptosystem,
i.e. key generation, encryption and decryption.

Uses primes.bin to read primes and stringConversion.py to convert strings to
numbers and reverse.

Main functionality in RSA.py. Run:


* To display help:
```
python RSA.py help
```

 * To generate a keypair:
 ```
 python RSA.py generate
 ```

 * To encrypt a text message:
 ```
 python RSA.py encrypt publicKeyE publicKeyN message
 ```
 
  * to decrypt a numerical message (output of above command):
 ```
 python RSA.py decrypt privateKeyP publicKeyN numerical
 ```
 
 * DO NOT USE for any real or practical applications. *
 This is not intended to be a safe system, it only serves as a demonstration.
