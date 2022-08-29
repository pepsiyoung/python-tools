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
    check_requirements('vvv')
