import hashlib
import glob


def read_binary_file(path):
    """Read a binary file specified by 'path' and print contents to console"""
    # print(" Opening file for reading " + path)
    f = open(path, 'rb')
    content = f.read()  # Read entire file
    f.close()
    #  print(content)
    return content  # <--- str() converts the binary data to a string


def md5(path):
    return hashlib.md5(read_binary_file(path))

def sha1(path):
    return hashlib.sha1(read_binary_file(path))

def sha256(path):
    return hashlib.sha256(read_binary_file(path))
