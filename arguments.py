""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 16/02/2021"""
import hashlib
import glob
import argparse
import pandas as pd
from datetime import datetime
import platform

def read_binary_file(path):
    """Reads a binary file specified by 'path' and print contents to console."""
    file = open(path, 'rb')
    content = file.read()  # Read entire file
    file.close()
    md5_hash = hashlib.md5(content).hexdigest()
    sha256_hash = hashlib.sha256(content).hexdigest()
    sha1_hash = hashlib.sha1(content).hexdigest()
    return str(md5_hash) + " " + str(sha256_hash) + " " + str(sha1_hash)


def search_function(column, search_term):
    if dataframe_list.__contains__(column) is True:
        search = list(dataframe[column])
        for i in dataframe.index:
            if search[i].__contains__(search_term) is True:
                if search_term == "path parts":
                    search_list = dataframe[column][i]
                    if search_list.__contains__(search_term) is True:
                        print(dataframe.iloc[i]) # have this print in table
                print(dataframe.iloc[i]) # have this print in table
            i += 1
    else:
        print("Sorry, that is an invalid column type")

operating_system = platform.system()
operating_system_version = platform.release()
target = "/home/anthony/"  # this sets the target directory
slash = ""
if operating_system == "Windows":
    if operating_system_version in (8, 8.1, 10):
        names = glob.glob(target + '**\\*.*',
                          recursive=True)  # this goes through every file path inside of the directory
        slash = "\\"
elif operating_system == "Linux":
    names = glob.glob(target + '**/*.*', recursive=True)  # this goes through every file path inside of the directory
    slash = "/"
hashed_dict = {}
"""This portion of the code checks to see if the database file exists. If not, it will create the database and 
    then allow a user to search the newly created database."""
for i in range(0, len(names)):
    """This creates the entries for the dictionary with the index being the full paths and the
    column info being hashes"""
    try:
        hashed_dict[names[i]] = read_binary_file(names[i])
    except IsADirectoryError or KeyError or FileNotFoundError:
        pass

# Database Generation and manipulation
dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
dataframe[['md5', 'sha256', 'sha1']] = dataframe['hashes'].str.split(expand=True)  # splits hashes column
dataframe.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
dataframe[['path parts']] = dataframe['full file paths'].str.split(slash)
dataframe_list = list(dataframe.columns)
now = datetime.now()
file_name = "IHDB_" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".csv"
dataframe.to_csv(file_name)  # converts dataframe to a csv file
print("New database saved as " + file_name)

# Argparse begins here
"""From here on, the following are assumed unless told otherwise via user flag:
-File name is the just created file as it is the most current
-No columns are specified therefore all columns will be searched for the program
-The only thing the user needs to provide is the search term
-If no flag is provided you just want to log and thus only a databse will be created"""

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--database", help="Specify database",
                    action="store_true")
parser.add_argument("-l", "--list", help="List existing databases",
                    action="store_true")
parser.add_argument("-c", "--hash", help="Search by checksum",
                    action="store_true")

args = parser.parse_args()
if args.database:
    args.database()

if args.list:
    db_list = glob.glob("*")
    for i in range(0, len(db_list)):
        if db_list[i].__contains__("IHDB"):
            print(db_list[i])
        i += 1

if args.hash:
    if args.hash().len(32) is True:
        search_function("md5", args.hash())

    elif args.hash().len(40) is True:
        search_function("sha1", args.hash())

    else:
        search_function("sha256", args.hash())




print("Thank you for using Information Hoarder")
