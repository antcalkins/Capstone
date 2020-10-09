import hashlib
import glob
import pandas as pd

target = "/home/writer/"
names = glob.glob(target + '**/*.*', recursive=True)
hashed_dict = {}


for i in range(0, len(names)):
    hashed_dict[names[i]] = str(hashlib.md5(names[i].encode('utf-8')).hexdigest()) + " " + \
                            str(hashlib.sha256(names[i].encode('utf-8')).hexdigest()) + " " + \
                            str(hashlib.sha1(names[i].encode('utf-8')).hexdigest())

dataframe = pd.DataFrame(list(hashed_dict.items()), columns=['file names', 'hashes'])
dataframe[['md5', 'sha256', 'sha1']] = dataframe['hashes'].str.split(expand=True)
dataframe.drop(['hashes'], axis=1, inplace=True)
print(dataframe.info())
print(dataframe.head())
dataframe.to_csv("dataframe.csv")


