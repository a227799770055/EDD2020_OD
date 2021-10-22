import os, cv2
path=r'C:\Users\eddie.hsiao\Documents\Eddie_Personal\yolo_test\EndoCV2020-Endoscopy-Disease-Detection-Segmentation-subChallenge_data\originalImages'

lis=os.listdir(path)
for i in lis:
    p=os.path.join(path,i)
    img=cv2.imread(p)
    print(img.shape)
