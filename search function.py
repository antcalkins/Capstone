import pandas as pd

dataframe = pd.read_csv("dataframe2.csv")
print(dataframe.head(10))
print(list(dataframe.columns))
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

column = "full file paths"
search_term = ".png"

search_function(column, search_term)
"""
value = input("What are you searching for? Type h for Hashes or f for file part. F includes "
              "file exentions.")
# searching path path parts
if value is "f":
    search_term = input("file part")
    for i in dataframe.index:
        search = list(dataframe["path parts"].loc[i])
        for j in range(0, len(search)):
            if search[-j].__contains__(search_term) is True:
                print("found it")
                print(dataframe.iloc[i])
            j += 1
        i += 1
    if i == dataframe.index[-1]:
        print("all done")
else:
    search_term = input("hash")
    for i in dataframe.index:
        search = list(dataframe["md5"].loc[i])
        for j in range(0, len(search)):
            if search[-j].__contains__(search_term) is True:
                print("found it")
                print(dataframe.iloc[i])
            j += 1
        i += 1
    for i in dataframe.index:
        search = list(dataframe["sha1"].loc[i])
        for j in range(0, len(search)):
            if search[-j].__contains__(search_term) is True:
                print("found it")
                print(dataframe.iloc[i])
            j += 1
        i += 1
    for i in dataframe.index:
        search = list(dataframe["sha256"].loc[i])
        for j in range(0, len(search)):
            if search[-j].__contains__(search_term) is True:
                print("found it")
                print(dataframe.iloc[i])
            j += 1
        i += 1
    if i == dataframe.index[-1]:
        print("all done")
"""
