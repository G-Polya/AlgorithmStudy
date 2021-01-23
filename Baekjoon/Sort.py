import hashlib
import os
f = open("C:\Program Files\Docker\Docker\InstallerCli.exe", 'rb')
data = f.read()
f.close()

print("CRC32: "+hashlib.)
print("MD5: " + hashlib.md5(data).hexdigest().upper())
print("SHA-1: " + hashlib.sha1(data).hexdigest().upper())
print("SHA-256: " + hashlib.sha256(data).hexdigest().upper())