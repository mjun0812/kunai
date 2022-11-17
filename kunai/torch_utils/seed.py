import random

import numpy as np


def is_available(func):
    def wrapper(*args, **kwargs):
        global torch, cudnn
        try:
            import torch

            return func(*args, **kwargs)
        except (ImportError, TypeError):
            print("Please install torch `pip install torch`")
            return

    return wrapper


@is_available
def worker_init_fn(worker_id):
    """Reset numpy random seed in PyTorch Dataloader

    Args:
        worker_id (int): random seed value
    """
    # random
    # random.seed(random.getstate()[1][0] + worker_id)
    # Numpy
    np.random.seed(np.random.get_state()[1][0] + worker_id)
    # torch.manual_seed(np.random.get_state()[1][0] + worker_id + 1)
    # torch.cuda.manual_seed_all(np.random.get_state()[1][0] + worker_id)


@is_available
def fix_seed(seed):
    """fix seed on random, numpy, torch module

    Args:
        seed (int): seed parameter

    Returns:
        int: seed parameter
    """
    # random
    random.seed(seed)
    # Numpy
    np.random.seed(seed)
    # Pytorch
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    return seed
