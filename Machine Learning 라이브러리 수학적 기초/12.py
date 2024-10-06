import numpy as np
import torch

X = np.array([[25, 2,], [5, 26], [3, 7]])
print(X)
print(X.T)

X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])
print(X_pt)
print(X_pt.T)

