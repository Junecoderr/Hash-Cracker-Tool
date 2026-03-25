import hashlib
import sys
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Hash Generator")
print(ascii_banner)
print("Algorithms available: MD5, SHA1, SHA256, SHA512")
hash_type = str(input("Enter the hash type you want to use: ")).upper()
wordlist_location = str(input("Enter the location of the wordlist: "))
hash = str(input("Enter the hash you want to crack: "))
word_list = open(wordlist_location, "r").readlines()
lists = word_list.splitlines()
for word in lists:
    if hash_type == "MD5":
        hash_object = hashlib.md5(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[132, HASH FOUND: {word} \n")

    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[132, HASH FOUND: {word} \n")
    elif hash_type == "SHA256":
        hash_object = hashlib.sha256(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[132, HASH FOUND: {word} \n")
    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[132, HASH FOUND: {word} \n")
    elif hash_type == "SHA3_256":
        hash_object = hashlib.sha3_256(word.encode('utf-8'))
        hashed = hash_object.hexdigest()
        if hash == hashed:
            print(f"\033[132, HASH FOUND: {word} \n")
    else:
        print("Please choose from the give")

