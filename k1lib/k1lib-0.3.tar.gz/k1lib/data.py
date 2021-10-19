# AUTOGENERATED FILE! PLEASE DON'T EDIT
import torch as _torch, math as _math, k1lib as _k1lib, os as _os
import numpy as _np, matplotlib.pyplot as _plt
from functools import partial as _partial
from typing import Iterator as _Iterator, Callable as _Callable, Tuple as _Tuple
from typing import Union as _Union, List as _List, overload as _overload
class DataLoader:
    @_overload
    def __init__(self, dataset, batchSize:int=32, transform:_Callable=None, random=True):
        """For official construction"""
        ...
    def __init__(self, dataset, batchSize:int=32, transform:_Callable=None, random=True, _slice:slice=slice(None)):
        """Creates a random sampler.

Basically, when given a dataset with length n and
batch size, this will split things up into n/batchSize
batches. Then, when indexed by an integer, this will
return a range of the dataset.

:param dataset: any object that implements __getitem__() and __len__()
    batchSize: integer

.. deprecated:: 0.1.3
        """
        self.dataset = dataset; self.batchSize = batchSize; self.random = random
        self.idxs = _np.random.permutation(len(dataset)) if random else list(range(len(dataset)))

        batches = _math.ceil(len(self.idxs) / batchSize)
        self._slice = _k1lib.Range(_slice, batches)
        self.idxs = self.idxs[(self._slice * batchSize).slice_]
        self.batches = _math.ceil(len(self.idxs) / batchSize)
        self.transform = transform if transform != None else (lambda x: x)
    def __len__(self) -> int: return self.batches
    def copy(self): return DataLoader(self.dataset, self.batchSize, self.transform, self.random, self._slice.slice_)
    def __getitem__(self, i:_Union[int, slice]) -> _Tuple[_torch.Tensor, _torch.Tensor]:
        if isinstance(i, slice):
            return DataLoader(self.dataset, self.batchSize, self.transform, self.random, self._slice[i].slice_)
        idxs:_List[int] = self.idxs[i*self.batchSize:(i+1)*self.batchSize]
        xs, ys = [], []
        for idx in idxs:
            x, y = self.dataset[idx]; x = self.transform(x)
            if not isinstance(x, _torch.Tensor): x = _torch.tensor(x)
            if not isinstance(y, _torch.Tensor): y = _torch.tensor(y)
            xs.append(x); ys.append(y)
        return _torch.stack(xs), _torch.stack(ys)
    def __iter__(self): return (self[i] for i in range(self.batches))
    def __repr__(self):
        return f"""DataLoader object. {len(self)} batches total, can...
- len(dl): to get number of batches the sampler has
- dl[:80]: to get a new DataLoader with only the first 80 batches
- dl[2]: to get the third batch
- for data in dl: print(data)
- it = iter(dl); data = next(it)"""
class Data:
    def __init__(self, train:DataLoader, valid:DataLoader):
        """Just a shell of both these variables really. Also, you can use
PyTorch's :class:`torch.utils.data.DataLoader` here just fine"""
        self.train = train; self.valid = valid
    @staticmethod
    def fromDataset(dataset, batchSize:int=32, trainSplit=0.8, *args, **kwargs):
        dl = DataLoader(dataset, batchSize, *args, **kwargs)
        m = _math.ceil(len(dl)*0.8); return Data(dl[:m], dl[m:])
    def __iter__(self):
        yield self.train
        yield self.valid
    def __repr__(self):
        return "`Data` object, just a shell containing 2 `DataLoader`s: `.train` and `.valid`"
@_k1lib.patch(_torch.utils.data.DataLoader)
def __repr__(self):
    return "DataLoader of:\n" + _k1lib.tab(self.dataset.__repr__())
class FunctionDataset(_torch.utils.data.Dataset):
    """
    A dataset tailored for 1->1 functions. Have several
    prebuilt datasets:
    - `.exp`: e^x
    - `.log`: ln(x)
    - `.inverse`: 1/x
    - `.linear`: 2x + 8
    - `.sin`: sin(x)
    """
    def __init__(self, function: callable, _range=[-5, 5], samples: int=300):
        """Creates a new dataset, with a specific function.

:param function: first order function, takes in an `x` variable
:param _range: range of x
:param samples: how many x in specified range
"""
        self.function = function
        self._range = _k1lib.Range(_range); self.samples = samples
        self._xsCache = None; self._ysCache = None
    def __len__(self): return self.samples
    def __getitem__(self, index):
        if isinstance(index, slice):
            nRange = _k1lib.Range([0, len(self)])
            _range = _k1lib.Range(index.start if index.start != None else self._range[0], index.stop if index.stop != None else self._range[1])
            samples = round(self._range.toRange(nRange, _range.stop)) - round(self._range.toRange(nRange, _range.start))
            return FunctionDataset(self.function, _range=_range, samples=samples)
        else:
            if index >= len(self): raise StopIteration(f"Out of bounds: {index}")
            x = index/self.samples * (self._range[1] - self._range[0]) + self._range[0]
            return _torch.tensor([x], dtype=_torch.bfloat16), _torch.tensor(self.function(x), dtype=_torch.bfloat16)
    def split(self, fraction):
        middle = self._range.fromUnit(fraction)
        return self[:middle], self[middle:]
    @property
    def xs(self):
        if self._xsCache == None:
            self._xsCache = _torch.Tensor([elem[0].item() for elem in self])
        return self._xsCache
    @property
    def ys(self):
        if self._ysCache == None:
            self._ysCache = _torch.Tensor([elem[1] for elem in self])
        return self._ysCache
    def dl(self, shuffle=True, batch_size=32, **kwargs):
        return _torch.utils.data.DataLoader(self, shuffle=shuffle, batch_size=batch_size, **kwargs)
    def __repr__(self):
        if int(_os.getenv("SPHINX", "0")) == 0:
            _plt.plot(self.xs, self.ys, "."); _plt.show()
        return """Simple 1->1 function dataset. Can do:
- a.dl(): to get PyTorch's DataLoader object
- a.xs: to get a tensor of all x values
- a.ys: to get a tensor of all y values
- len(a): to get length of dataset
- a[i]: to get specific (x, y) element
- a[a:b]: to get another FunctionDataset with a new range [a, b] (same density)
- next(iter(a)): to iterate over all elements"""
FunctionDataset.exp = FunctionDataset(lambda x: _np.exp(x), samples=10000)
FunctionDataset.log = FunctionDataset(lambda x: _np.log(x), _range=[0.01, 5], samples=10000)
FunctionDataset.inverse = FunctionDataset(lambda x: 1/x, samples=10001)
FunctionDataset.linear = FunctionDataset(lambda x: 2*x+8, samples=10000)
FunctionDataset.sin = FunctionDataset(lambda x: _np.sin(x), samples=10000)
class CyclicRandomSampler:
    def __init__(self, n):
        """Samples from a dataset randomly. If runs out of elements then reset."""
        self.n = n
    def __iter__(self):
        while True: yield from _torch.randperm(self.n)
class DatasetWithSampler:
    """Yields ds's elements with a specified sampler"""
    def __init__(self, ds, sampler): self.ds = ds; self.sampler = sampler
    def __iter__(self):
        for e in self.sampler: yield self.ds[e]
    def __len__(self): return len(self.ds)