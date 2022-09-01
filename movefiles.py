import os
import shutil

source="C:/Users/trish/Downloads"
destination="C:/Users/trish/Downloads"
listoffiles=os.listdir(source)


for i in listoffiles:
    root,ext=os.path.splitext(i)
    if ext =="":
        continue
    if ext in [".txt",".doc",".docx",".pdf"]:
        path1=source+"/"+i
        path2=destination+"/"+"documents"
        path3=destination+"/"+"documents"+"/"+i
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
