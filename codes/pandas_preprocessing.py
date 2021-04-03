import pandas as pd
import datetime
import numpy as np

##date data processing
#string to datetime
df['date_data'] = pd.to_datetime(df['date_data'])

#make a datediff coloumn(do not passing null data on calculating)
df['date_diff'] = base_date - pd.to_datetime(df['date_data'][~df['date_data'].isnull()])
df['date_diff_years'] = df['date_diff'] / np.timedelta64(1, Y)
#df['date_diff_months'] = df['date_diff'] / np.timedelta64(1, M)
#df['date_diff_days'] = df['date_diff'] / np.timedelta64(1, D)

##word data hot encoding
#make a word list
df_word = df['word_data'][~df['word_data'].isnull()]
word_list = []
for num in range(0, len(df_word)):
    s = df_word[int(num)]
    #l = s.split(',')
    l = [x.strip() for x in s.split(',') if not x.strip() == '']
    word_list.extend(l)

#word_list = sorted(set(word_list), key=word_list.index)
word_list = list(dict.fromkeys(filter(None, word_list)))

#make word columns
df['word_flag'] = 1
for word in word_list:
    df[str(word)] = df[word_flag][df['word_data'].fillna("").str.contains(str(word))]


##extra
#make code coloumn
df = df.reset_index()
df['data_no'] = df['level_0'].str.zfill(6)

#function from using one coloumn
def fun_num2(num):
    if num <= 26:
        return chr(64+num)
    elif num%26==0:
        return num2(num//26-1)+chr(90)
    else:
        return num2(num//26) + chr(64+num%26)
df['num'] = df['num'].fillna("").apply(fun_num2)

#function from using one coloumn on simply case
df['num'] = df['num'].fillna("").apply(lambda x : 1 if x >= 1 else 0)

#function from using multiple coloumn
def fun_comparing(x):
    if x['compare_base'] == x['compare_target']:
        return 'same'
    else:
        return 'diff'
df['compare_col'] = df[['compare_base', 'compare_target']].fillna("").apply(fun_comparing, axis=1)