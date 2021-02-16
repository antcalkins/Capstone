""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 16/02/2021"""
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
    if dataframe_list.__contains__(column) is True:
        search = list(dataframe[column])
        for i in dataframe.index:
            if search[i].__contains__(search_term) is True:
                print("found it")
                print(dataframe.iloc[i])
            i += 1
    else:
        print("Sorry, that is an invalid column type")


if path.exists("dataframe2.csv") is False:
    """This portion of the code checks to see if the database file exists. If not, it will create the database and 
    then allow a user to search the newly created database."""
    for i in range(0, len(names)):
        """This creates the entries for the dictionary with the index being the full paths and the
        column info being hashes"""
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
    search_start = input("Would you like to search the database? Type 'y' for yes or 'n' for no")
    while search_start is 'y':
        dataframe_list = list(dataframe.columns)
        print(dataframe_list)
        column = input("What column would you like to search?")
        search_term = input("Put your search term here")
        search_function(column, search_term)
        search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no")


else:
    """If the database file already exists, this portion of the code will run. It starts by asking if the user wants 
    to update the database."""
    dataframe = pd.read_csv("dataframe2.csv")
    dataframe_list = list(dataframe.columns)
    database_update = input("Would you like to update the database? Type 'y' for yes or 'n' for no ")
    if database_update is 'y':
        for i in range(0, len(names)):
            """This creates the entries for the dictionary with the index being the full paths and the
            column info being hashes"""
            try:
                hashed_dict[names[i]] = str(md5(names[i])) + " " + str(sha256(names[i])) + " " + str(sha1(names[i]))
            except IsADirectoryError or KeyError:
                pass

        # Database Generation and manipulation
        dataframe2 = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
        dataframe2[['md5', 'sha256', 'sha1']] = dataframe2['hashes'].str.split(expand=True)  # splits hashes column
        dataframe2.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
        dataframe2[['path parts']] = dataframe2['full file paths'].str.split("/")
        dataframe2.to_csv("dataframe_updated.csv")  # converts dataframe to a csv file
        dataframe = dataframe2
    search_start = input("Would you like to search the database? Type 'y' for yes or 'n' for no ")
    while search_start is 'y':
        print(dataframe_list)
        column = input("What column would you like to search? ")
        search_term = input("Put your search term here: ")
        search_function(column, search_term)
        search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no ")

print("Thank you for using Information Hoarder")
