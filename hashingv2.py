""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 13/02/2021"""
import hashlib
import glob
import pandas as pd
from os import path

target = "/home/writer/"  # this sets the target directory
names = glob.glob(target + '**/*.*', recursive=True)  # this goes through every file path inside of the directory
hashed_dict = {}  # this is where the hashed files will be stored


def read_binary_file(path):
    """Reads a binary file specified by 'path' and print contents to console"""
    # print(" Opening file for reading " + path)
    file = open(path, 'rb')
    content = file.read()  # Read entire file
    file.close()
    # print(content)
    return content  # converts the binary data as bytes


def md5(path):
    """Returns the MD5 hash of the input path's associated file"""
    return hashlib.md5(read_binary_file(path)).hexdigest()


def sha1(path):
    """Returns the SHA1 hash of the input path's associated file"""
    return hashlib.sha1(read_binary_file(path)).hexdigest()


def sha256(path):
    """Returns the SHA256 hash of the input path's associated file"""
    return hashlib.sha256(read_binary_file(path)).hexdigest()


def search_function(column, search_term):
    dataframe_list = list(dataframe.columns)
    if dataframe_list.__contains__(column) is True:
        for i in dataframe.index:
            search = list(dataframe[column])
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


if path.exists("dataframe2.csv") is False:
    for i in range(0, len(names)):
        # this creates the entries for the dictionary with the index being the full paths and the
        # column info being hashes
        try:
            hashed_dict[names[i]] = str(md5(names[i])) + " " + str(sha256(names[i])) + " " + str(sha1(names[i]))
        except IsADirectoryError or KeyError:
            pass

    # Database Generation and manipulation
    dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
    dataframe[['md5', 'sha256', 'sha1']] = dataframe['hashes'].str.split(expand=True)  # splits hashes column
    dataframe.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
    dataframe[['path parts']] = dataframe['full file paths'].str.split("/")
    # Database design check
    # print(dataframe.info())
    # print(dataframe.head())
    dataframe.to_csv("dataframe2.csv")  # converts dataframe to a csv file
    print("file made :)")
    search_start = input("Would you like to search the database? type 'y' for yes or 'n' for no")
    while search_start is 'y':
        dataframe_list = list(dataframe.columns)
        print(dataframe_list)
        column = input("What column would you like to search?")
        search_term = input("Put your search term here")
        search_function(column, search_term)
        search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no")


else:
    search_start = input("Would you like to search the database? type 'y' for yes or 'n' for no")
    dataframe = pd.read_csv("dataframe2.csv")
    dataframe_list = list(dataframe.columns)
    while search_start is 'y':
        print(dataframe_list)
        column = input("What column would you like to search?")
        search_term = input("Put your search term here")
        search_function(column, search_term)
        search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no")
print("Thank you for using Information Hoarder")
