import pandas as pd
import regex
import glob


def create_filename():
    """Create filename list from os.listdir()"""

    filelist = []
    colname_list = []

    for file in glob.glob('./data/*.txt'):
        colname_list.append(file[12:-4])
        filelist.append(file)

    return filelist, colname_list

filelist, colname_list = create_filename()

x = 0
df = pd.DataFrame()

for file in filelist:
    TEXT = []
    with open(file, 'r') as f:
        text = f.readlines()
        for txt in text:
            if txt != '\n':
                TEXT.append(txt)

    colname = colname_list[x]
    df[colname] = pd.Series(TEXT)
    x += 1

df.to_csv("blog_spot.csv")
