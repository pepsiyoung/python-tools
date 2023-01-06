from thop import profile
import torch
from torchvision.models import resnet18
# import models.yolo as yolo


model = resnet18()
# model = yolo.Model(cfg='models/yolov5x.yaml')
#
m_input = torch.randn(1, 3, 8192, 8192)  # 模型输入的形状,batch_size=1
flops, params = profile(model, inputs=(m_input,))
print(flops / 1e12, params / 1e6)  # flops单位T，para单位M
