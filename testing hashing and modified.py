from datetime import datetime
import hashlib
from os import scandir


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def read_binary_file(path):
    """Reads a binary file specified by 'path' and print contents to console."""
    file = open(path, 'rb')
    content = file.read()  # Read entire file
    file.close()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()
    sha1_hash = hashlib.sha1(content).hexdigest()
    if path.is_file():
        info = file.stat()
    return str(md5_hash) + " " + str(sha256_hash) + " " + str(sha1_hash) + " " + str(convert_date(info))


def get_files():
    dir_entries = scandir('/home/writer/')
    output = []
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            output.append(convert_date(info.st_mtime))
    return output

# get_files()
print(get_files())