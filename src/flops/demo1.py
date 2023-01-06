import torch
from torchvision import models
from torchstat import stat
from thop import profile

# print('Pytorch version\t:', torch.__version__)
# print('CUDA version\t:', torch.version.cuda)
# print('GPU\t\t\t\t:', torch.cuda.get_device_name())
#
# if __name__ == '__main__':
#     net = models.mobilenet_v2()
#     stat(net, (3, 8192, 8192))


if __name__ == '__main__':
    net = models.mobilenet_v2()
    inputs = torch.randn(1, 3, 8192, 8192)
    flops, params = profile(net, inputs=(inputs,))
    print("FLOPs=", str(flops / 1e9) + '{}'.format("G"))
    print("params=", str(params / 1e6) + '{}'.format("M"))
