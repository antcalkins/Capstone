""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 04/03/2021"""
import hashlib
import glob
import pandas as pd
import platform
from os import path
# import argparse


operating_system = platform.system()
operating_system_version = platform.release()
target = input("Enter target directory: ")  # this sets the target directory
slash = ""
if operating_system == "Windows":
    if operating_system_version in (8, 8.1, 10):
        names = glob.glob(target + '**\\*.*',
                          recursive=True)  # this goes through every file path inside of the directory
        slash = "\\"
elif operating_system == "Linux":
    names = glob.glob(target + '**/*.*', recursive=True)  # this goes through every file path inside of the directory
    slash = "/"
"""
To properly implement this portion of the code, likes 60-119 need to become part of a def main.
else:
    print("This os is not supported, we cannot guarantee that it will work, do you wish to proceed?")
    check = input("Type 'y' for yes or 'n' for no: ")
    """
hashed_dict = {}  # this is where the hashed files will be stored


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


if path.exists("dataframe2.csv") is False:
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
    dataframe.to_csv("dataframe2.csv")  # converts dataframe to a csv file
    print("file made :)")
    search_start = input("Would you like to search the database? Type 'y' for yes or 'n' for no ")
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
        # merge files
        for i in range(0, len(names)):
            """This creates the entries for the dictionary with the index being the full paths and the
            column info being hashes"""
            try:
                hashed_dict[names[i]] = read_binary_file(names[i])
            except IsADirectoryError or KeyError or FileNotFoundError:
                pass

        # Database Generation and manipulation
        dataframe2 = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
        dataframe2[['md5', 'sha256', 'sha1']] = dataframe2['hashes'].str.split(expand=True)  # splits hashes column
        dataframe2.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
        dataframe2[['path parts']] = dataframe2['full file paths'].str.split(slash)
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
