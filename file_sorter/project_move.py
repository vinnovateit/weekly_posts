import shutil
import os
from pathlib import Path
files = []
listy=[]
listu=[]
existing=[]
# r=root, d=directories, f = files

#give root directory of folder containing downloads
path=r"path where your files are being donwloaded"
for r, d, f in os.walk(path):
    for file in d:
        existing.append(file)
    for file in f:
        if r==path:
            files.append(file)
#create folders for subject codes
for f in files:
    if(f[0:4]=="FALL"):
        listy.append(f[15:22])
    elif (f[0:3]=="WIN"):
        listy.append(f[14:21])


#create directories got non existing folders
for i in range(0,len(listy)):
    if listy[i] not in listu and listy[i] not in existing:
        listu.append(listy[i])
        path =r"Path where you want your folder to be created"
        pathy=path.rstrip()+listy[i]
        print(pathy)
        os.mkdir(pathy) 

path=r"path where your files are being donwloaded"   

#move to respective folders
for i in range(0,len(listy)):
    for r,d,f in os.walk(path):
        for file in f:
            print(r,file)
            if os.path.join(r, file).find(listy[i])>=0 and r==path:
                dirr=r"Path where you want your folder to be created"
                dirry=dirr.rstrip()+listy[i]
                shutil.move(os.path.join(r,file),os.path.join(dirry,file))

                
             





  
