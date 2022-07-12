import json
import os
import argparse
from tqdm import tqdm
from pathlib import Path, PurePath
from PIL import Image
import time
import torch
import torch.nn as nn


# class MyModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = nn.Conv2d(1, 10, 5)  # 输入通道数1，输出通道数10，核的大小5
#         self.conv2 = nn.Conv2d(10, 20, 3)  # 输入通道数10，输出通道数20，核的大小3
#
#     def forward(self, x):
#         out = self.conv1(x)  # batch*1*28*28 -> batch*10*24*24（28x28的图像经过一次核为5x5的卷积，输出变为24x24）
#         return out


model = torch.load('/Users/pepsiyoung/Project/my/Jupyter/torchLearning/model/my_model_with_arc.pth')
model.eval()
print(model)
