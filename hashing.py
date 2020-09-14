import hashlib


def read_binary_file(path):
    """Read a binary file specified by 'path' and print contents to console"""
    # print(" Opening file for reading " + path)
    f = open(path, 'rb')
    content = f.read()  # Read entire file
    f.close()
    #  print(content)
    return content  # <--- str() converts the binary data to a string


def hash(path):
    md5 = hashlib.md5(read_binary_file(path))
    sha1 = hashlib.md5(read_binary_file(path))
    sha256 = hashlib.md5(read_binary_file(path))
    return {"path": path, "md5": md5, "sha1": sha1, "sha256": sha256}
