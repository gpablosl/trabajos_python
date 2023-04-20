import hashlib

a = hashlib.sha1(b"ClaseCompresionDatos")
b = hashlib.sha224(b"ClaseCompresionDatos")
c = hashlib.sha256(b"ClaseCompresionDatos")
d = hashlib.sha384(b"ClaseCompresionDatos")
e = hashlib.sha512(b"ClaseCompresionDatos")

f = hashlib.blake2b(b"ClaseCompresionDatos")
g = hashlib.blake2s(b"ClaseCompresionDatos")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
