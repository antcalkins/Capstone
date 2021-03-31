from datetime import datetime
import hashlib
from os import scandir
import os
import glob

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d/%b/%Y %H:%M:%S')
    return formated_date


def read_binary_file(path):
    """Reads a binary file specified by 'path' and print contents to console."""
    file = open(path, 'rb')
    content = file.read()  # Read entire file
    file.close()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()
    sha1_hash = hashlib.sha1(content).hexdigest()
    stat = os.stat(path)
    return str(md5_hash) + " " + str(sha256_hash) + " " + str(sha1_hash) + " " + str(convert_date(stat.st_mtime))


def get_files():
    dir_entry = scandir('/home/writer')
    output = []
    for entry in dir_entry:
        if entry.is_file():
            info = entry.stat()
            output.append(convert_date(info.st_mtime))
    return output

target = '/home/writer/'
names = glob.glob(target + '**/*.*', recursive=True)
print(read_binary_file("hashing.py"))
# print(get_files())
# file ='/home/writer/PycharmProjects/Capstone/hashing.py'
# print(names[0])
# stat = os.stat(file)
# print(stat.st_mtime)
