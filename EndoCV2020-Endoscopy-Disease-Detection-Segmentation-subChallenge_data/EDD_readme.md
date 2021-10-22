## Endoscopy Disease Detection and Segmentation Challenge (EDD2020)

[Link to EDD2020 webpage](https://edd2020.grand-challenge.org/Home/)

**About data**

This released version consists of **386** endoscopy frames from 5 different institutions and multi-GI organs. The data set consists of masked image annotations and bounding boxes for disease detection, localization and semantic segmentation tasks. The dataset was used in EndoCV2020 challenge for sub-challenge EDD2020. The data is released under licence: **Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).** Please cite below papers if you use this data. 

**References:**

[1]  Ali, S., Dmitrieva, M., Ghatwary, N. et al. Deep learning for detection and segmentation of artefact and disease instances in gastrointestinal endoscopy. Medical Image Analysis, 2021. [URL](https://doi.org/10.1016/j.media.2021.102002)
 
[2] Ali, S., Ghatwary, N.M., Braden, B., Lamarque, D., Bailey, A., Realdon, S.,
Cannizzaro, R., Rittscher, J., Daul, C., East, J., 2020b. Endoscopy disease
detection challenge 2020. CoRR abs/2003.03376.  [URL](https://arxiv.org/abs/2003.03376)

[Related challenge proceeding](http://ceur-ws.org/Vol-2595/) 

**Features**

[1] Annotated data consists of 5 different disease classes
``BE, suspicious, HGD, cancer, polyp`` (see *class_list.txt* in the folder)

[2] Each image file is annotated for single or multiple disease classes

[3] Same disease class is merged in masks while kept as separate bounding boxes for detection task

[4] Bounding boxes are presented in VOC format. Please see [fileFormatConverters of EAD2019](https://github.com/sharibox/EAD2019/tree/master/fileFormatConverters)

[5] Details on data will soon be released and provided on arxiv

[6] Getting started: we encourage to use [EAD2019 github tool](https://github.com/sharibox/EAD2019). We are working in compiling a separate software to help you with it.

[7] Please note that you will have to replace 'class_list.txt' with the new one. Additionally, please add this information in the code where required 


**Contact**

Lead organiser: [Dr. Sharib Ali](sharib.ali@eng.ox.ac.uk)

**Acknowledgment:** Special thanks to *Prof. Barbara Braden* and *Noha Ghatwary* for their time in helping us compile this dataset

**Disclaimer:** The data and information provided is for research purpose only. You should not rely upon the data provided for direct usage in softwares for disease detection. The accuracy, reliability and completeness of the annotations may be subjective to the annotators.
