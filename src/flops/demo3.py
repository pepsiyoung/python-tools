# from thop import profile
# import torch
# import models.yolo as yolo


# # model = resnet18()
# model = yolo.Model(cfg='models/yolov5x.yaml')
#
# m_input = torch.randn(1, 3, 640, 3584)  # 模型输入的形状,batch_size=1
# flops, params = profile(model, inputs=(m_input,))
# print(flops / 1e9, params / 1e6)  # flops单位G，para单位M
