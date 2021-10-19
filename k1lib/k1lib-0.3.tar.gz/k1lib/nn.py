# AUTOGENERATED FILE! PLEASE DON'T EDIT
import torch.nn as _nn
from typing import Callable as _Callable, Any as _Any
class Lambda(_nn.Module):
    def __init__(self, f:_Callable[[_Any], _Any]):
        """Creates a simple module with a specified :meth:`forward`
function."""
        super().__init__(); self.f = f
    def forward(self, x): return self.f(x)
class Identity(Lambda):
    """Creates a module that returns the input in :meth:`forward`"""
    def __init__(self): super().__init__(lambda x: x)