import pandas as pd

df_changed = pd.read_csv('master_changed2.csv', dtype='str')
df = df_changed.head(20)
print(df['generation'].unique())
print(df[df['generation'].isnull()])

def num2(num):
    if num <= 26:
        return chr(64+num)
    elif num%26==0:
        return num2(num//26-1)+chr(90)
    else:
        return num2(num//26) + chr(64+num%26)

KESSON = 'kesson'

category_list = ['generation']

for name in category_list:
    df[name] = df[name].fillna(KESSON)
    unique_category = list(df[name].unique())
    print(unique_category)
    print(zip(unique_category))
    #print(list(map(num2, list(range(1, len(unique_category)+1)))))
    category_mapping = dict(zip(unique_category, list(map(num2, list(range(1, len(unique_category)+1))))))
    print(category_mapping)
    df[name] = df[name].map(category_mapping)

print(df[df['generation'].isnull()])

df = df_changed.head(20)
for name in category_list:
    unique_category = list(df[name].unique())
    print(unique_category)
    print(zip(unique_category))
    #print(list(map(num2, list(range(1, len(unique_category)+1)))))
    category_mapping = dict(zip(unique_category, list(map(num2, list(range(1, len(unique_category)+1))))))
    print(category_mapping)
    df[name] = df[name][~df[name].isnull()].map(category_mapping)
    print(df[name].unique())

print(df[df['generation'].isnull()])