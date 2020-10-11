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

for i in range(0, len(names)):
    # this creates the entries for the dictionary with the index being the full paths and the column info being hashes
    hashed_dict[names[i]] = str(hashlib.md5(names[i].encode('utf-8')).hexdigest()) + " " + \
                            str(hashlib.sha256(names[i].encode('utf-8')).hexdigest()) + " " + \
                            str(hashlib.sha1(names[i].encode('utf-8')).hexdigest())

dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['full file paths', 'hashes'])  # creates dataframe
dataframe[['md5', 'sha256', 'sha1']] = dataframe['hashes'].str.split(expand=True)  # splits hashes column
dataframe.drop(['hashes'], axis=1, inplace=True)  # drops the unnecessary hashes column
dataframe[['path parts']] = dataframe['full file paths'].str.split("/")
# print(dataframe.info())
# print(dataframe.head())
dataframe.to_csv("dataframe.csv")  # converts dataframe to a csv file
print("file made :)")
value = "lyall.sh"
print(list(dataframe["path parts"].loc[27]))
# searching path path parts
for i in dataframe.index:
    search = list(dataframe["path parts"].loc[i])
    if search.__contains__(value) is True:
        print("found it")
        print(dataframe.iloc[i])
    i += 1
    if i == dataframe.index[-1]:
        print("all done")
