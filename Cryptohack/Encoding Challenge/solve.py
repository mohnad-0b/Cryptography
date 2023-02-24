from pwn import *
import json
import codecs
#  nc socket.cryptohack.org 13377
io = remote('socket.cryptohack.org', 13377)

for _ in range(100):
    
    DATA = io.recvline().decode()
    type = (json.loads(DATA)["type"])
    encoded = (json.loads(DATA)["encoded"])

    if type == "base64":
        decoded = base64.b64decode(encoded)
    elif type == "hex":
        decoded = bytes.fromhex(encoded)
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot_13').encode()
    elif type == "bigint":
        decoded = bytes.fromhex(encoded[2:])
    elif type == "utf-8":
        decoded = ("".join([chr(b) for b in encoded])).encode()
    io.sendline(b'{"decoded" :"' +  decoded + b'"}')

print(json.loads(io.recvline())['flag'])
# crypto{3nc0d3_d3c0d3_3nc0d3}
