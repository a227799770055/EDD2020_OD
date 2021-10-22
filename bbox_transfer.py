import numpy as np 
import os

bbox_path = r'.\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\bbox'
bbox_yolo_path=r'.\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\bbox_yolotype'

types=['BE', 'suspicious', 'HGD', 'cancer', 'polyp']

#read file_name 
bbox_files=os.listdir(path=bbox_path)
for i in bbox_files:
    box=[]
    path=os.path.join(bbox_path, i)
    with open(path, "r") as f:
        for line in f.readlines():
            line = line.split(' ')
            x_0 = int(line[0])
            y_0 = int(line[1])
            x_1 = int(line[2])
            y_1 = int(line[3])

            w=(x_0+x_1)/2
            h=(y_0+y_1)/2
            xc=x_0+w
            yc=y_0+h
            type = types.index(line[4][:-1])
            box.append([type, xc, yc, w, h])
    
    #另存路徑
    o_path=os.path.join(bbox_yolo_path, i)
    with open(o_path, "w") as f:
        for line in box:
            f.write(" ".join('%s' %id for id in line)+"\n")
print("finish convert")