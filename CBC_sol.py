from pwn import *
from base64 import *
r = remote('140.110.112.191',4120)
def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

cipher = r.recvline().strip()
cipher = b64decode(cipher)
iv = cipher[:16]

new_iv = xor(xor(iv,b'A'*16),b'CTFGOGOGO0000000')
new_cipher = new_iv + cipher[16:]
new_cipher2 = cipher[16:] + new_iv
print(new_cipher2)
print(new_cipher)
new_cipher = b64encode(new_cipher)

r.sendline(new_cipher)
r.interactive()
