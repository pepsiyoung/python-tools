from PIL import Image
from pathlib import Path
import yaml
from tqdm import tqdm


def test(func):
    def handler(*args, ):
        print('test')
        func(*args)

    return handler


def say_hello(country):
    def wrapper(func):
        def decorate(*args, **kw):
            print('country:', country)
            func(*args, **kw)

        return decorate

    return wrapper


# def try_except(func):
#     # try-except function. Usage: @try_except decorator
#     def handler(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#         except Exception as e:
#             print(e)
#
#     return handler


# @test
country = 'usa'


@say_hello(country)
def check_requirements(name):
    print('check_requirements:' + name)


if __name__ == '__main__':
    check_requirements('zcy')
    check_requirements('ccc')
