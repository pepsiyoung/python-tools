from PIL import Image
from pathlib import Path
import yaml
from tqdm import tqdm


def test(func):
    def handler(*args, ):
        print('test')
        func(*args)

    return handler


# def try_except(func):
#     # try-except function. Usage: @try_except decorator
#     def handler(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as e:
#             print(e)
#
#     return handler


@test
def check_requirements(name):
    print('check_requirements:' + name)


if __name__ == '__main__':
    # check_requirements('vvv')
    values_cnt = {}

    l_count = 0
    other_count = 0
    im_path = r'D:\datasets\CSI_0901\images'
    im_paths = Path(im_path).glob('**/*.jpg')
    for im_path in tqdm(list(im_paths)):
        im = Image.open(im_path)
        # im.convert("RGB").save(Path("D:\\datasets\\CSI_0901\\images_rgb").joinpath(im_path.name))

        if im.mode == 'L':
            l_count += 1
        else:
            other_count += 1

    print('l_count:', l_count)
    print('other_count:', other_count)
