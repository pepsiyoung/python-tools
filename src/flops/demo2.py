import inspect
from collections import defaultdict
import pandas as pd
import torch
from torch.utils import benchmark

pd.options.display.precision = 3


def var_dict(*args):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return dict([(name, val) for name, val in callers_local_vars if val is arg][0]
                for arg in args)


def wall_time(stem, arg_dict, duration=10):
    return benchmark.Timer(stem, globals=arg_dict).blocked_autorange(min_run_time=duration).median


matmul_tflops = defaultdict(lambda: {})
for n in [128, 512, 2048, 8192]:
    for dtype in (torch.float32, torch.float16):
        a = torch.randn(n, n, dtype=dtype).cuda()
        b = torch.randn(n, n, dtype=dtype).cuda()
        t = wall_time('a @ b', var_dict(a, b))
        matmul_tflops[f'n={n}'][dtype] = 2 * n ** 3 / t / 1e12
        del a, b

res = pd.DataFrame(matmul_tflops)
print(res)

# callers_local_vars = inspect.currentframe().f_back.f_locals.items()
# print(callers_local_vars)


