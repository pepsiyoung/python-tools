import cv2
import os
from PIL import Image

xml_head = '''<annotation>
    <folder>VOC2007</folder>
    <!--文件名-->
    <filename>{}</filename>.
    <source>
        <database>csi</database>
    </source> 
    <size>
        <width>{}</width>
        <height>{}</height>
        <depth>1</depth>
    </size>
    <segmented>0</segmented>
    '''
xml_obj = '''
    <object>        
        <name>xuhan</name>
        <pose>Rear</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>{}</xmin>
            <ymin>{}</ymin>
            <xmax>{}</xmax>
            <ymax>{}</ymax>
        </bndbox>
    </object>
    '''
xml_end = '''
</annotation>'''

labels = ['xuhan', 'xuhan', 'xuhan']  # label for datasets

cnt = 0

jpg = r'F:\deep-learning\datasets\YOLO可训练数据\NEU-DET\train\images\crazing_1.jpg'  # image path
txt = r'F:\deep-learning\datasets\YOLO可训练数据\NEU-DET\train\labels\crazing_1.txt'  # yolo label txt path
xml_path = r'C:\Users\pozhe\Downloads\crazing_1.xml'  # xml save path

obj = ''

# img = cv2.imread(jpg)
# img_h, img_w = img.shape[0], img.shape[1]
img = Image.open(jpg)
img_h, img_w = img.size

head = xml_head.format(str(jpg), str(img_w), str(img_h))
with open(txt, 'r') as f:
    for line in f.readlines():
        yolo_datas = line.strip().split(' ')
        label = int(float(yolo_datas[0].strip()))
        center_x = round(float(str(yolo_datas[1]).strip()) * img_w)
        center_y = round(float(str(yolo_datas[2]).strip()) * img_h)
        bbox_width = round(float(str(yolo_datas[3]).strip()) * img_w)
        bbox_height = round(float(str(yolo_datas[4]).strip()) * img_h)

        xmin = str(int(center_x - bbox_width / 2))
        ymin = str(int(center_y - bbox_height / 2))
        xmax = str(int(center_x + bbox_width / 2))
        ymax = str(int(center_y + bbox_height / 2))

        obj += xml_obj.format(labels[label], xmin, ymin, xmax, ymax)
with open(xml_path, 'w') as f_xml:
    f_xml.write(head + obj + xml_end)
cnt += 1
print(cnt)
