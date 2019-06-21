# since version 2.5: Use the hashlib module instead.
import hashlib

m = hashlib.md5()
word = "123".encode("utf-8")
m.update(word)
dg = m.digest()
print(dg)
hexdg = m.hexdigest()
print(hexdg)
