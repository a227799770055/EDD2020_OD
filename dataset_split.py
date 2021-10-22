import numpy as np
import os

image_path=r'.\data'
f=os.listdir(image_path)
split_ratio=0.8

img_=[]
#只取 .jpg 後綴的檔案
for i in f:
    if os.path.splitext(i)[1] == '.jpg':
        p=os.path.join(image_path,i)
        img_.append(p)

#打亂順序
np.random.shuffle(img_)
len_=len(img_)
len_=int(split_ratio*len_)
img_train=img_[:len_]
img_test=img_[len_:]


dataset=['img_train.txt', 'img_test.txt']
data=[img_train, img_test]
for i, n in zip(dataset, data):
    p=os.path.join(image_path, i)
    with open(p, 'w') as f:
        for line in n:
            f.write("".join('%s' %id for id in line)+"\n")

