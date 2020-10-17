import os
import re
os.chdir('C:/Users/Kuldeep saini/Desktop/auto_renamer/main') # change it
filelist = os.listdir()
text = 0
file_type = '.mp4'
number_of_videos = len(filelist)
for range_for_splittext in range(len(filelist)):
    for files in filelist:
        number = re.findall('[0-9]{2}\s',filelist[range_for_splittext])
        if os.path.splitext(files)[1] == file_type:
            videos_name = os.path.splitext(files)[0]
            ignoring_alerady_renamed = re.findall('^#',filelist[range_for_splittext])
            if ignoring_alerady_renamed[range_for_splittext] not in filelist:
                os.rename(filelist[range_for_splittext],f"#{number[0]}{videos_name}{file_type}")
            else:
                print("Error on rename")
        else:
            print("Somthing Went Wrong")
