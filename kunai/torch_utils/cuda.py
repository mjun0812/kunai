import os
import time

import torch
from torch.backends import cudnn


def set_device(global_gpu_index, is_cpu=False, pci_device_order=True):
    """Set use GPU or CPU Device

    set using GPU or CPU Device(instead of CUDA_VISIBLE_DEVICES).
    set also CUDNN.

    Args:
        global_gpu_index (int): using gpu number in all gpu.
        is_cpu (bool, optional): use cpu or not. Defaults to False.
        pci_device_order (bool, optional): . Defaults to True.

    Returns:
        torch.device: use device object.
    """

    if not is_cpu:
        if pci_device_order:
            os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = str(global_gpu_index)

        # print using GPU Info
        cuda_info(int(str(global_gpu_index).split(",")[0]))
        print("Using GPU is CUDA:{}".format(global_gpu_index))

        if cudnn.is_available():
            cudnn.benchmark = True
            torch.backends.cudnn.deterministic = True  # 乱数固定のため
            print("Use CUDA, CUDNN")
        else:
            print("Use CUDA")
        device = torch.device("cuda:0")
    else:
        device = torch.device("cpu")
        print("Use CPU")

    return device


def cuda_info(global_cuda_index=0):
    """show using GPU Info

    Args:
        global_cuda_index (int, optional): using GPU number in all GPU number. Defaults to 0.
    """
    for i in range(torch.cuda.device_count()):
        info = torch.cuda.get_device_properties(i)
        print(f"CUDA:{i + global_cuda_index} {info.name}, {info.total_memory / 1024 ** 2}MB")


def time_synchronized():
    """return time at synhronized CUDA and CPU.
       CUDAとCPUの計算が非同期なため，同期してから時間計算する．

    Returns:
        time: 関数呼び出し時の時刻
    """
    # pytorch-accurate time
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return time.time()
