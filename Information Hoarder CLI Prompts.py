""" This code is designed to hash files and create a pandas dataframe that can be referenced by a graphical interface
and modified by the user. Presently it is not attached to a gui, and therefore runs natively within an environment such
as pycharm, where it functions as a program prompted command line tool. There is no Path Parts.
Authors: L.E. Rogers and A.B. Calkins
Last Edited: 04/03/2021"""
import hashlib
import glob
import pandas as pd
import platform
from datetime import datetime
import os

"""This portion of the code detects what operating system a user is running the program on. It can set variables by 
detecting if it is running on windows or on linux."""
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
hashed_dict = {}  # this is where the hashed files will be stored


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


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    format_date = d.strftime('%d/%b/%Y_%H:%M:%S')
    return format_date


def search_function(column, search_term):
    """This search function takes in two string inputs column and search_term.
    Column refers to the column of the database that a user wants to search.
    Search_term is the specific search term."""
    if dataframe_list.__contains__(column) is True:
        # search is the list of the columns in the dataframe
        search = list(dataframe[column])
        for i in dataframe.index:
            if search[i].__contains__(search_term) is True:
                print(dataframe.iloc[i])  # have this print in table
            i += 1
    else:
        print("Sorry, that is an invalid column type")


# This checks to see if there are any database files on the system
dir_list = glob.glob("*")
db_list = []
database_exists = False
for i in range(0, len(dir_list)):
    if dir_list[i].__contains__("IHDB"):
        database_exists = True
        db_list.append(dir_list[i])
    i += 1

if database_exists is False:
    """This portion of the code checks to see if the database file exists. If not, it will create the database and 
    then allow a user to search the newly created database."""
    for i in range(0, len(names)):
        """This creates the entries for the dictionary with the index being the full paths and the
        column info being hashes"""
        try:
            hashed_dict[names[i]] = str(i) + " " + read_binary_file(names[i])
        except IsADirectoryError or KeyError or FileNotFoundError:
            pass

    # Database Generation and manipulation
    dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
    dataframe[['index', 'md5', 'sha256', 'sha1', 'modified date-time']] = dataframe['hashes'].str.split(expand=True)  # splits hashes column
    dataframe.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
    df_dups = dataframe[dataframe.duplicated(['md5', 'sha256', 'sha1'])]
    print(df_dups.columns)
    dups = df_dups['index']
    duplicates = []
    for i in range(0, len(dataframe)):
        if i in dups:
            duplicates.append('True')
        else:
            duplicates.append('False')
    dataframe['duplicates'] = duplicates
    now = datetime.now()
    file_name = "IHDB_" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".csv"
    dataframe.to_csv(file_name)  # converts dataframe to a csv file
    print("File made")
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
    print(db_list)
    dataframe = pd.read_csv(db_list[0])
    dataframe_list = list(dataframe.columns)
    database_update = input("Would you like to update the database? Type 'y' for yes or 'n' for no: ")
    if database_update is 'y':
        merger = input("Would you like to update the "
                       "database or create a new file? Type 'c' for create and 'm' for merge: ")
        if merger.lower() == 'c':
            for i in range(0, len(names)):
                """This creates the entries for the dictionary with the index being the full paths and the
                column info being hashes"""
                try:
                    hashed_dict[names[i]] = str(i) + " " + read_binary_file(names[i])
                except IsADirectoryError or KeyError or FileNotFoundError:
                    pass
            # Database Generation and manipulation
            # creates dataframe
            dataframe2 = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])
            dataframe2[['index', 'md5', 'sha256', 'sha1', 'modified date-time']] = dataframe2['hashes'].str.split(expand=True)  # splits hashes column
            dataframe2.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
            df_dups = dataframe2[dataframe2.duplicated(['md5', 'sha256', 'sha1'])]
            dups = df_dups['index']
            duplicates = []
            for i in range(0, len(dataframe2)):
                if i in dups:
                    duplicates.append("True")
                else:
                    duplicates.append("False")
            dataframe2['duplicates'] = duplicates
            now = datetime.now()
            file_name = "IHDB_" + now.strftime("%d-%m-%Y_%H-%M-%S") + ".csv"
            dataframe2.to_csv(file_name)  # converts dataframe to a csv file
            dataframe = dataframe2
        else:
            for i in range(0, len(names)):
                """This creates the entries for the dictionary with the index being the full paths and the
                column info being hashes"""
                try:
                    hashed_dict[names[i]] = str(i) + " " + read_binary_file(names[i])
                except IsADirectoryError or KeyError or FileNotFoundError:
                    pass
            # Database Generation and manipulation
            dataframe2 = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])
            dataframe2[['md5', 'sha256', 'sha1', 'modified date-time']] = dataframe2['hashes'].str.split(expand=True)
            dataframe2.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
            df_dups = dataframe2[dataframe2.duplicated(['md5', 'sha256', 'sha1'])]
            dups = df_dups['index']
            duplicates = []
            for i in range(0, len(dataframe2)):
                if i in dups:
                    duplicates.append("True")
                else:
                    duplicates.append("False")
            dataframe2['duplicates'] = duplicates
            concatenated = pd.concat([dataframe, dataframe2])
            concatenated.drop_duplicates()
            concatenated.to_csv(db_list[0])
            print("Merge successful")
            dataframe = concatenated

    search_start = input("Would you like to search the database? Type 'y' for yes or 'n' for no ")
    while search_start is 'y':
        print(dataframe_list)
        column = input("What column would you like to search? ")
        search_term = input("Put your search term here: ")
        search_function(column, search_term)
        search_start = input("Do you still want to search? Type 'y' for yes and 'n' for no ")

print("Thank you for using Information Hoarder")
