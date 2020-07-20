from pwn import *
from base64 import *

r = remote('140.110.112.191',4121)

def register(username,password):
    r.sendlineafter(b'> ','1')
    r.sendlineafter('username: ',username)
    r.sendlineafter('password: ',password)
    token = r.recvline().strip()
    return token

def login(token):
    r.sendlineafter(b'> ','2')
    r.sendlineafter(b'token: ',token)

username = b'a' *6
password = b'a' *7 +b'username:admin;password:'+b'a'*8
token = register(username,password)
token = b64decode(token)
new_token = token[32:]
new_token = b64encode(new_token)
login(new_token)

r.interactive()

