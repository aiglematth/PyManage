from Crypto.PublicKey import RSA
from hashlib import md5
from .saveAndLoad import save
from .proto_com import *

a = RSA.generate(4096)
b = RSA.generate(4096)

mess = {"dechiffrer":a.exportKey().decode(), "chiffrer":b.publickey().exportKey().decode()}

save(mess, "keys.txt")

c = RSA.generate(4096)
d = RSA.generate(4096)

mess = {"dechiffrer":d.exportKey().decode(), "chiffrer":c.publickey().exportKey().decode()}

save(mess, "hiskeys.txt")

mess = "a"*(512-33)
mess += f":{md5(mess.encode()).hexdigest()}"
mess = a.publickey().encrypt(d.publickey().encrypt(mess.encode(), None)[0], None)[0]

print(Get_code(mess).code)
