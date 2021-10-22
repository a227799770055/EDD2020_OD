import PIL
import cv2 
import torch

image_path = r".\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\originalImages\EDD2020_AJ0001.jpg"
bbox_path = r".\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\bbox\EDD2020_AJ0001.txt"


def read_img():
    boxs=[]
    with open(bbox_path) as f:
        for line in f.readlines():
            line = line.split(' ')
            x_0 = int(line[0])
            y_0 = int(line[1])
            x_1 = int(line[2])
            y_1 = int(line[3])
            type = line[4][:-1]
            boxs.append([x_0,y_0,x_1,y_1])
    print(boxs)
    #代表左下到右上

    
    img = cv2.imread(image_path)
    


    for i in boxs:
        cv2.rectangle(img, (i[0],i[1]), (i[2], i[3]), (0, 255, 0), 2)   
    cv2.imshow('My Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    read_img()