import numpy as np 
import os
import cv2

bbox_path = r'.\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\bbox'
bbox_yolo_path=r'.\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\bbox_yolotype'
i_path=r'C:\Users\eddie.hsiao\Documents\Eddie_Personal\yolo_test\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\originalImages'
types=['BE', 'suspicious', 'HGD', 'cancer', 'polyp']

#read file_name 
def type_transfer():
    bbox_files=os.listdir(path=bbox_path)
    for i in bbox_files:
        box=[]
        path=os.path.join(bbox_path, i)
        img_path=os.path.join(i_path, i.replace('.txt', '.jpg'))

        #取得圖片大小
        shap=cv2.imread(img_path).shape
        y_shap=shap[0]
        x_shap=shap[1]
        

        with open(path, "r") as f:
            for line in f.readlines():
                line = line.split(' ')
                x_0 = float(line[0])/x_shap
                y_0 = float(line[1])/y_shap
                x_1 = float(line[2])/x_shap
                y_1 = float(line[3])/y_shap

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

if __name__ == '__main__':
    type_transfer()