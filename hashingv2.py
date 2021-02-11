""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 09/10/2020
"""
import hashlib
import glob
import pandas as pd

target = "/home/writer/"  # this sets the target directory
names = glob.glob(target + '**/*.*', recursive=True)  # this goes through every file path inside of the directory
hashed_dict = {}  # this is where the hashed files will be stored


def read_binary_file(path):
    try:
        """Read a binary file specified by 'path' and print contents to console"""
        # print(" Opening file for reading " + path)
        file = open(path, 'rb')
        content = file.read()  # Read entire file
        file.close()
        # print(content)
        return content #converts the binary data as bytes
    except IsADirectoryError:
        pass


def md5(path):
    """Returns the MD5 hash of the input path's associated file"""
    return hashlib.md5(read_binary_file(path))


def sha1(path):
    """Returns the SHA1 hash of the input path's associated file"""
    return hashlib.sha1(read_binary_file(path))


def sha256(path):
    """Returns the SHA256 hash of the input path's associated file"""
    return hashlib.sha256(read_binary_file(path))

# functions check
# print(names[6])
# print(md5(names[6]))


for i in range(0, len(names)):
    # this creates the entries for the dictionary with the index being the full paths and the column info being hashes
    hashed_dict[names[i]] = str(md5(names[i])) + str(sha256(names[i])) + str(sha1(names[i]))
    print(hashed_dict[names[i]])

# Database Generation and manipulation
dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
dataframe[['md5', 'sha256', 'sha1']] = dataframe['hashes'].str.split(expand=True)  # splits hashes column
dataframe.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
dataframe[['path parts']] = dataframe['full file paths'].str.split("/")
# Database design check
# print(dataframe.info())
# print(dataframe.head())
dataframe.to_csv("dataframe.csv")  # converts dataframe to a csv file
# print("file made :)")

##########################


def search_function(column, search_term):
    # This is the search function that allows a user to search the databse
    # Column is a string that specifies the specific column in the dataframe
    # search_term is a string that is the specific search parameter such as a file name, file extension, hash,
    # or file path
    if column is "full file paths" or column is "md5" or column is "sha1" or column is "sha256" \
            or column is "path parts":
        for i in dataframe.index:
            search = list(dataframe[column].loc[i])
            for j in range(0, len(search)):
                if search[-j].__contains__(search_term) is True:
                    print("found it")
                    print(dataframe.iloc[i])
                j += 1
            i += 1
        if i == dataframe.index[-1]:
            print("all done!")
    else:
        print("That is an invalid column to search in, sorry :(")


search_start = input("Would you like to search the database? type 'y' for yes or 'n' for no")
while search_start is 'y':
    print(dataframe.head)
    column = input("What column would you like to search?")
    search_term = input("Put your search term here")
    search_function(column, search_term)
    search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no")

