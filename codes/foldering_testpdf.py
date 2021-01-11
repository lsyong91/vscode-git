import glob
import os
import shutil
#test
from_path = "/Users/seungyong/workspace/workspace/project1/downloads/test_pdf"
to_path = "/Users/seungyong/workspace/workspace/project1/downloads"
txtfiles = []
for file in glob.glob(path + "/*.pdf"):
    txtfiles.append(file)

#making directory
year_list = ['2015', '2016', '2017', '2018', '2019', '2020']
season_list = ['h', 'a']
for year in year_list:
    for season in season_list:
        if season == 'h':
            os.makedirs(to_path + "/" + str(year)+'春')
        if season == 'a':
            os.makedirs(to_path + "/" + str(year)+'秋')
        for afile in txtfiles:
            if str(year) in afile:
                if season == 'h':
                    if 'h_ap' in afile:
                        basename = os.path.basename(afile)
                        shutil.move(afile, to_path + "/" + str(year)+'春/'+basename)
                    else:
                        pass
                elif season == 'a':
                    if 'a_ap' in afile:
                        basename = os.path.basename(afile)
                        shutil.move(afile, to_path + "/" + str(year)+'秋/'+basename)
                    else:
                        pass