from PIL import Image
import argparse


def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='./source', help='')
    return parser.parse_known_args()[0] if known else parser.parse_args()


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
    opt = parse_opt(True)
    im = Image.open(opt.source)
    im.show()
