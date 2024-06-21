import torch.nn as nn
import torch
class Softmax(nn.Module):
  def __init__(self) -> None:
    super(Softmax, self).__init__()

  def forward(self, data):
    # mũ e cho từng phần tử
    exps = torch.exp(data)
    sum_exps = torch.sum(exps)
    # chia total cho từng phần tử
    return exps / sum_exps

class SoftmaxStable(nn.Module):
  def __init__(self) -> None:
    super(SoftmaxStable, self).__init__()

  def forward(self, data):
    # dim : muốn xét theo chiều nào, mattrix 1 chiều thì dim = 0 sẽ là hàng, 2 chiều dim = 0 là cột/ dim = 1 là hàng
    # keepdim có muốn giữ chiều return theo dim kh
    c = torch.max(data, dim=0, keepdim=True)
    exps = torch.exp(data - c.values)
    sum_exps = exps.sum(dim=0, keepdim=True)
    return exps / sum_exps


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax.forward(data)
print(output)

softmax_stable = SoftmaxStable()
output = softmax_stable.forward(data)
print(output)
