from Crypto.PublicKey import RSA
from Crypto.Util.number import *
rsa = RSA.importKey(open('babyRSA.pem').read())
#print(rsa.n)
#print(rsa.e)
c = open('flag.enc','rb').read()
c = bytes_to_long(c)
n = 86044608266042558038553786299703811809507347936888618532703612396944160396661
e = 65537
p =270613060120468613971049355250995010949
q =317961772531370599800029965079161987889
phi = (p-1)*(q-1)
d = inverse(e,phi)
m = pow(c,d,n)
print(long_to_bytes(m))
