import torch
import torchvision
from torch.utils.data import Dataset
from torch.utils.data import DataLoader


class MyDataset(Dataset):
    # 构造函数
    def __init__(self, data_tensor, target_tensor):
        self.data_tensor = data_tensor
        self.target_tensor = target_tensor

    # 返回数据集大小
    def __len__(self):
        return self.data_tensor.size(0)

    # 返回索引的数据与标签
    def __getitem__(self, index):
        return self.data_tensor[index], self.target_tensor[index]


def get_MNIST():
    # 以MNIST为例
    mnist_dataset = torchvision.datasets.MNIST(root='/Users/pepsiyoung/Project/my/Jupyter/data', train=True,
                                               transform=None, target_transform=None,
                                               download=True)


if __name__ == '__main__':
    # 生成数据
    data_tensor = torch.randn(10, 3)
    target_tensor = torch.randint(2, (10,))  # 标签是0或1

    # 将数据封装成Dataset
    my_dataset = MyDataset(data_tensor, target_tensor)

    # 查看数据集大小
    print('Dataset size:', len(my_dataset))
    # 使用索引调用数据
    print('tensor_data[0]: ', my_dataset[0])

    print('----------------')
    tensor_data_loader = DataLoader(dataset=my_dataset, batch_size=2, shuffle=True, num_workers=0)
    # # 以循环形式输出
    # for data, target in tensor_data_loader:
    #     print(data, target)

    # print('One batch tensor data: ', iter(tensor_data_loader).next())
    # my_iter = iter(tensor_data_loader)
    # print('iter', next(my_iter))
