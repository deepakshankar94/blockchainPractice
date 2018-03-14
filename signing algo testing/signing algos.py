from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
rng = Random.new().read
RSAkey = RSA.generate(1024, rng)   # This will take a while...
print(RSAkey)
hash = MD5.new("plaintext".encode()).digest()
signature = RSAkey.sign(hash, rng)
print(signature)   # Print what an RSA sig looks like--you don't really care.
print(RSAkey.verify(hash, signature))     # This sig will check out
print(RSAkey.verify(hash[:-1], signature))# This sig will fail
print(repr(RSAkey.publickey()))