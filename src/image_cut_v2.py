import yaml
from PIL import Image
from pathlib import Path, PurePath


def parse_opt():
    with open('./config_v2.yaml', 'r', encoding="utf-8") as f:
        file_data = f.read()
        data = yaml.load(file_data, Loader=yaml.FullLoader)
        return data


def makedir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


# 边框剪裁
def padding_cut(image: Image, padding_box):
    image_w, image_h = image.size
    padding_top, padding_right, padding_bottom, padding_left = padding_box
    padding_cut_img = image.crop((0 + padding_left, 0 + padding_top, image_w - padding_right, image_h - padding_bottom))
    print('边框裁剪完成')
    return padding_cut_img


def auto_cut(image: Image, file_name: str):
    cut_weight, cut_height = tuple(args.get('cutSize').values())
    coverage = args.get('coverage', 0)
    bias_list = args.get('bias')
    bias_dict = dict(zip([item['num'] for item in bias_list], [item['px'] for item in bias_list]))
    w, h = image.size
    cut_count = round(w / (cut_weight - coverage))
    # 创建文件夹
    save_path = "./target/{0}".format(file_name)
    makedir(save_path)
    x1, y1, x2, y2 = 0, 0, cut_weight, cut_height
    for index in range(cut_count):
        x_stride = 0 if index == 0 else cut_weight - coverage
        x_bias = bias_dict.get(index + 1, 0)
        x1 = x1 + x_stride + x_bias
        x2 = x2 + x_stride + x_bias
        processed_im = image.crop((x1, y1, x2, y2))
        # 保存图片
        processed_im.save("{0}/{1}.jpg".format(save_path, index + 1))
    print('自动裁剪完成')


# 全局变量参数
args = {}

if __name__ == "__main__":
    print('正在切图请耐心等待。。。')
    # 获取配置文件参数
    args = parse_opt()
    print('参数:{}'.format(args))

    p = Path(args.get('sourceFolder'))
    source_img_list = [x for x in p.iterdir() if PurePath(x).match('*.jpeg') or PurePath(x).match('*.jpg')]

    for img_path in source_img_list:
        print('原图:{}'.format(img_path))
        origin_im = Image.open(img_path)
        padding_cut_im = padding_cut(origin_im, tuple(args.get('padding').values()))
        auto_cut(padding_cut_im, Path(img_path).stem)
    input("<切图完成,按任意键退出>")
