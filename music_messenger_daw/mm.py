from cryptography.fernet import Fernet

key1 = Fernet.generate_key()
key2 = Fernet.generate_key()

print(key1.decode())
print(key2.decode())