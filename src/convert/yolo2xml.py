from PIL import Image
from pathlib import Path, PurePath
from tqdm import tqdm


def convert(txt, img_w, img_h):
    obj = ''
    name = Path(txt).stem
    head = xml_head.format('{}.jpg'.format(name), img_w, img_h)
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

    xml_path = r'F:\deep-learning\datasets\YOLO可训练数据\CSI-虚焊-292\train\xml'
    with open(Path(xml_path).joinpath('{}.xml'.format(name)), 'w') as f_xml:
        f_xml.write(head + obj + xml_end)


xml_head = '''<annotation>
    <folder>VOC2007</folder>
    <!--文件名-->
    <filename>{}</filename>.
    <source>
        <database>CSI</database>
    </source> 
    <size>
        <width>{}</width>
        <height>{}</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    '''
xml_obj = '''
    <object>        
        <name>{}</name>
        <pose>Unspecified</pose>
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

im_paths = r'F:\deep-learning\datasets\YOLO可训练数据\CSI-虚焊-292\train\images'
txt_paths = Path(r'F:\deep-learning\datasets\YOLO可训练数据\CSI-虚焊-292\train\labels').glob('**/*.txt')
for txt_path in tqdm(list(txt_paths)):
    txt_name = Path(txt_path).stem
    img_path = Path(im_paths).joinpath('{}.jpg'.format(txt_name))
    if Path.exists(img_path):
        w, h = Image.open(img_path).size
        convert(txt_path, w, h)




