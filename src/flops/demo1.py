import torch

print('Pytorch version\t:', torch.__version__)
print('CUDA version\t:', torch.version.cuda)
print('GPU\t\t\t\t:', torch.cuda.get_device_name())
