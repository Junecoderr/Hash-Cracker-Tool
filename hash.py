import hashlib
import sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Generator")
print(ascii_banner)
print("Algorithms available: MD5, SHA1, SHA256, SHA512, SHA3_256")

hash_type = input("Enter the hash type you want to use: ").upper()
wordlist_location = input("Enter the location of the wordlist: ")
target_hash = input("Enter the hash you want to crack: ")

valid = {"MD5", "SHA1", "SHA256", "SHA512", "SHA3_256"}
if hash_type not in valid:
    print("Please choose from MD5, SHA1, SHA256, SHA512, SHA3_256")
    sys.exit(1)

try:
    with open(wordlist_location, "r") as f:
        words = f.read().splitlines()
except FileNotFoundError:
    print(f"Wordlist not found: {wordlist_location}")
    sys.exit(1)

found = False
for word in words:
    if hash_type == "MD5":
        hashed = hashlib.md5(word.encode()).hexdigest()
    elif hash_type == "SHA1":
        hashed = hashlib.sha1(word.encode()).hexdigest()
    elif hash_type == "SHA256":
        hashed = hashlib.sha256(word.encode()).hexdigest()
    elif hash_type == "SHA512":
        hashed = hashlib.sha512(word.encode()).hexdigest()
    elif hash_type == "SHA3_256":
        hashed = hashlib.sha3_256(word.encode()).hexdigest()
    else:
        continue

    if target_hash == hashed:
        print(f"\033[1;32m[+] HASH FOUND: {word}\033[0m")
        found = True
        break

if not found:
    print("\033[1;31m[-] Hash not found in wordlist.\033[0m")