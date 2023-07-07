from PIL import Image
from torchvision import transforms
import torch

# orig_img = Image.open('/Users/pepsiyoung/Downloads/aaa.jpg')
# orig_img = orig_img.convert("RGB")
# norm_operator = transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
# img_tensor = transforms.ToTensor()(orig_img)
# tensor_norm = norm_operator(img_tensor)
# # Tensor转化为图像
# img_norm = transforms.ToPILImage()(tensor_norm)
# img_norm.save('/Users/pepsiyoung/Downloads/bbb.jpg')


orig_img = Image.open('/Users/pepsiyoung/Downloads/bbb.jpg')
# orig_img = orig_img.convert("RGB")
# tensor_img = transforms.ToTensor()(orig_img)
# x = torch.where(tensor_img < 0.32, 0, tensor_img)
# target_img = transforms.ToPILImage()(x)
# target_img.save('/Users/pepsiyoung/Downloads/bbb.jpg')

# print(tensor_img[1, 300:900, 1200:2400])
# print(tensor_img[:, 300:800, 1200:2400])


# t = torch.tensor([[10, 20, 30], [15, 25, 35]])
# x = torch.where(t < 21, 0, t)
# print(x)
