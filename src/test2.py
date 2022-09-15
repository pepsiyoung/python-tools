class Father:
    def __init__(self):
        print('father')

    # def getName(self):
    #     return 'Father ' + self.name


class Son(Father):
    def __init__(self, name):
        super(Son, self).__init__()
        print("hi")
        self.name = name

    def getName(self):
        return 'Son ' + self.name


if __name__ == '__main__':
    son = Son('runoob')
    print(son.getName())
