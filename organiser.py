import os
import shutil
from_dir="C:/Users/DELL/Downloads"
to_dir="C:/Users/DELL/Class102"
listofFiles=os.listdir(from_dir)
print(listofFiles)

for file in listofFiles:
    name,ext=os.path.splitext(file)
    print(name)
    print(ext)
    if ext=="":
        continue
    if ext in [".pdf",".jpeg",".ini",".accdb",".zip",".exe",".jpg",".mp4"]:
        path1=from_dir +"/"+ file
        path2= to_dir +"/"+ext
        path3=path2+"/" +file
        
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)