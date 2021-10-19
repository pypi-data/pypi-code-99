# Copyright 2021 Yan Yan
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
from typing import Dict

import numpy as np
from pccm.targets.cuda_ptx import RegDType

from cumm.constants import CUTLASS_MODE


class DType(object):
    def __init__(self,
                 name: str,
                 num_bits: int,
                 shortcut: str,
                 tv_dtype: int,
                 reg_dtype: RegDType,
                 cutlass: str = ""):
        self._name = name
        self.num_bits = num_bits
        self._shortcut = shortcut
        self.tv_dtype = tv_dtype
        self._cutlass_name = cutlass
        self.reg_dtype = reg_dtype

    @property
    def cutlass(self) -> str:
        if self._cutlass_name:
            return self._cutlass_name
        return self._name

    def itemsize(self):
        assert self.num_bits >= 8
        return self.num_bits // 8

    def bitsize(self):
        return self.itemsize() * 8

    def shortcut(self):
        return self._shortcut

    @property
    def name(self) -> str:
        if CUTLASS_MODE:
            return self.cutlass
        else:
            return self._name

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: "DType"):
        return self.name == other.name

    def __ne__(self, other: "DType"):
        return self.name != other.name

    def npdtype(self):
        return get_npdtype(self)


float16 = DType("tv::half_t", 2 * 8, "f16", 1, RegDType.F16, "cutlass::half_t")
float32 = DType("float", 4 * 8, "f32", 2, RegDType.F32)
float64 = DType("double", 8 * 8, "f64", 3, RegDType.F64)
int8 = DType("int8_t", 1 * 8, "s8", 4, RegDType.S8)
int16 = DType("int16_t", 2 * 8, "s16", 5, RegDType.S16)
int32 = DType("int32_t", 4 * 8, "s32", 6, RegDType.S32)
int64 = DType("int64_t", 8 * 8, "s64", 7, RegDType.S64)
uint8 = DType("uint8_t", 1 * 8, "u8", 8, RegDType.U8)
uint16 = DType("uint16_t", 2 * 8, "u16", 9, RegDType.U16)
uint32 = DType("uint32_t", 4 * 8, "u32", 10, RegDType.U32)
uint64 = DType("uint64_t", 8 * 8, "u64", 11, RegDType.U64)
bfloat16 = DType("tv::bfloat16_t", 2 * 8, "bf16", 12, RegDType.BF16,
                 "cutlass::bfloat16_t")
tf32 = DType("tv::tfloat32_t", 4 * 8, "tf32", 13, RegDType.TF32,
             "cutlass::tfloat32_t")  # float32 with last 13 bit removed.

ALL_DTYPES = (float16, float32, float64, int8, int16, int32, int64, uint8,
              uint16, uint32, uint64, bfloat16, tf32)

SHORTCUT_TO_DTYPE = {d.shortcut(): d for d in ALL_DTYPES}

DTYPE_TO_NPDTYPE = {
    float16: np.dtype(np.float16),
    float32: np.dtype(np.float32),
    float64: np.dtype(np.float64),
    int8: np.dtype(np.int8),
    int16: np.dtype(np.int16),
    int32: np.dtype(np.int32),
    int64: np.dtype(np.int64),
    uint8: np.dtype(np.uint8),
    uint16: np.dtype(np.uint16),
    uint32: np.dtype(np.uint32),
    uint64: np.dtype(np.uint64),
    tf32: np.dtype(np.float32),
}  # type: Dict[DType, np.dtype]

NPDTYPE_TO_DTYPE = {v: k
                    for k, v in DTYPE_TO_NPDTYPE.items()
                    }  # type: Dict[np.dtype, DType]


def get_dtype_by_shortcut(shortcut: str):
    return SHORTCUT_TO_DTYPE[shortcut]


def get_npdtype(dtype: DType):
    return DTYPE_TO_NPDTYPE[dtype]


def get_dtype_from_npdtype(npdtype: np.dtype):
    return NPDTYPE_TO_DTYPE[npdtype]


if __name__ == "__main__":
    a = np.zeros((1, 2))
    print(type(a.dtype))
    print(type(np.uint8))
