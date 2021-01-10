import datetime
import os

d_today = datetime.date.today()

d_today

d_today_str = d_today.strftime('%y%m%d')

filename = 'RA_S'+ d_today_str + '.xlsx'
print(filename)

!pwd

filename = '/content/sample_data/README.md'
print(filename)

filename_cp = '/content/sample_data/README2.md'

!cp $filename $filename_cp

file = open("/content/sample_data/test/test1.txt", "w") 
file.write("test") 
file.close() 

!cp /content/sample_data/test/test1.txt /content/sample_data/test/test20201002.txt

file_list = []
for file in os.listdir("/content/sample_data/test/"):
  if file.endswith(".txt"):
    file_list.append(file)
print(file_list)

def last_4chars(x):
    return(x[-12:-4])

sorted_list = sorted(file_list, key = last_4chars)
print(sorted_list)