import torch
from torch import nn
from torch.nn import functional as F


class Residual(nn.Module):
    def __init__(self, input_channels, num_channels,
                 use_1x1conv=False, strides=1):
        super().__init__()
        self.conv1 = nn.Conv2d(input_channels, num_channels, kernel_size=3, padding=1, stride=strides)
        self.conv2 = nn.Conv2d(num_channels, num_channels, kernel_size=3, padding=1)
        if use_1x1conv:
            self.conv3 = nn.Conv2d(input_channels, num_channels, kernel_size=1, stride=strides)
        else:
            self.conv3 = None
        self.bn1 = nn.BatchNorm2d(num_channels)
        self.bn2 = nn.BatchNorm2d(num_channels)

    def forward(self, X):
        Y = F.relu(self.bn1(self.conv1(X)))
        Y = self.bn2(self.conv2(Y))
        if self.conv3:
            X = self.conv3(X)
        Y += X
        return F.relu(Y)


class SPPF(nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool = nn.MaxPool2d(5, 1, padding=2)

    def forward(self, x):
        o1 = self.maxpool(x)
        print('o1_shape', o1.shape)
        o2 = self.maxpool(o1)
        print('o2_shape', o2.shape)
        o3 = self.maxpool(o2)
        return torch.cat([x, o1, o2, o3], dim=1)


if __name__ == '__main__':
    input_tensor = torch.rand(8, 32, 16, 16)
    # sppf = SPPF()
    # output = sppf(input_tensor)
    # print(output.shape)

    net = nn.MaxPool2d(5, 1, padding=2)
    print(net(input_tensor).shape)
