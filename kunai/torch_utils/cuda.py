import os
import time


def is_available(func):
    def wrapper(*args, **kwargs):
        global torch, cudnn
        try:
            import torch
            from torch.backends import cudnn

            return func(*args, **kwargs)
        except (ImportError, TypeError):
            print("Please install torch `pip install torch`")
            return

    return wrapper


@is_available
def set_device(
    global_gpu_index,
    rank=-1,
    is_cpu=False,
    pci_device_order=True,
    cudnn_deterministic=False,
    verbose=True,
) -> torch.device:
    """Set use GPU or CPU Device

    set using GPU or CPU Device(instead of CUDA_VISIBLE_DEVICES).
    set also CUDNN.

    Args:
        global_gpu_index (int): using gpu number in all gpu.
        rank (int): process rank
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
        if verbose:
            cuda_info(int(os.environ["CUDA_VISIBLE_DEVICES"].split(",")[0]))
            print(f"Using GPU is CUDA:{global_gpu_index}")

        if cudnn.is_available():
            cudnn.benchmark = True
            cudnn.deterministic = cudnn_deterministic  # 乱数固定のため
            if verbose:
                print("Use CUDNN")
        if rank == -1:
            rank = 0
        device = torch.device(rank)
        torch.cuda.set_device(rank)
    else:
        device = torch.device("cpu")
        if verbose:
            print("Use CPU")

    return device


@is_available
def cuda_info(global_cuda_index=0):
    """show using GPU Info

    Args:
        global_cuda_index (int, optional): using GPU number in all GPU number. Defaults to 0.
    """
    for i in range(torch.cuda.device_count()):
        info = torch.cuda.get_device_properties(i)
        print(f"CUDA:{i + global_cuda_index} {info.name}, {info.total_memory / 1024 ** 2}MB")


@is_available
def time_synchronized() -> time:
    """return time at synhronized CUDA and CPU.
       CUDAとCPUの計算が非同期なため，同期してから時間計算する．

    Returns:
        time: 関数呼び出し時の時刻
    """
    # pytorch-accurate time
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return time.time()
