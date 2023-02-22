import torch

a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[1, 2], [2, 2]])

print(a.mm(b))


# 1 2
# 3 4

# 1 2
#   2 2