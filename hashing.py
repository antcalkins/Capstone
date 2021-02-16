import hashlib
import glob

target = input("Directory of interest:")
paths = glob.glob(target + '**/*.*', recursive=True)

###
def read_binary_file(path):
    """Read a binary file specified by 'path' and print contents to console"""
    # print(" Opening file for reading " + path)
    f = open(path, 'rb')
    content = f.read()  # Read entire file
    f.close()
    #  print(content)
    return content  # <--- str() converts the binary data to a string
###

def md5(path):
    """Returns the MD5 hash of the input path's associated file"""
    return hashlib.md5(read_binary_file(path))


def sha1(path):
    """Returns the SHA1 hash of the input path's associated file"""
    return hashlib.sha1(read_binary_file(path))


def sha256(path):
    """Returns the SHA256 hash of the input path's associated file"""
    return hashlib.sha256(read_binary_file(path))


print(paths)
