import random

import numpy as np

import torch


def worker_init_fn(worker_id):
    """Reset numpy random seed in PyTorch Dataloader

    Args:
        worker_id (int): random seed value
    """
    # random
    random.seed(random.getstate()[1][0])
    # Numpy
    np.random.seed(np.random.get_state()[1][0] + worker_id)


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
    torch.cuda.manual_seed_all(seed)
    return seed
