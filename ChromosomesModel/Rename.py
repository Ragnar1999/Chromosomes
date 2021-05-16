import os
path = "D:/Learn/大三下/summer/正常归类/hard data(11-21) - 副本/Hard Data"
filelist = os.listdir(path)
count=0
for file in filelist:
    print(file)
for file in filelist:
    Olddir=os.path.join(path,file)
    if os.path.isdir(Olddir):
        continue
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    Newdir=os.path.join(path,str(count).zfill(4)+filetype)
    os.rename(Olddir,Newdir)

    count+=1