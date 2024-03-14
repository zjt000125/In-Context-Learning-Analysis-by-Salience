# from functools import wraps, partial

# class MyClass:
#     def __init__(self):
#         self.data = 1234
#     def f(self, b=1):
#         print(b)

# def f_(b=0, c=None):
#     print(b)
#     print(c)

# test = MyClass()

# test.f = partial(f_, test, c = 'test')

# test.f()
import torch
import torch.nn.functional as F

# output = torch.tensor([0.5]).float()
# label = torch.tensor([0.9]).float()
# loss = F.cross_entropy(output, label)

# print(loss)

# 创建一个一维数组
input_array = torch.tensor([0.9, 0.8, 0.1, 0.2])

# 创建一个目标数组
target_array = torch.tensor([1, 1, 0, 0]).float()

# 计算交叉熵损失
loss = F.cross_entropy(input_array, target_array)

print(loss)