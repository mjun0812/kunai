import logging
import os

from torchinfo import summary

import torch
from torch.nn.parallel import DistributedDataParallel

logger = logging.getLogger()


def save_model(model, file_path):
    """Save PyTorch Model
    PyTorchのモデルを保存する
    Parallelにも対応

    Args:
        model (torch.nn.Module): モデルオブジェクト
        file_path (str): 保存先
    """
    if check_model_parallel(model):
        model = model.module
    torch.save(model.state_dict(), file_path)
    logger.info("Saving model at %s", file_path)


def save_model_info(output_dir, model, input_size, prefix=""):
    """Output PyTorch Model Summary to log.

    Args:
        output_dir (string): output log dir
        model (torch.nn.Module): PyTorch Model Class
        input_size (List): input tensor size
        prefix (str, optional): log file prefix output_dir/model_summary_{prefix}.log. Defaults to "".
    """
    if prefix:
        prefix = "_" + prefix
    if check_model_parallel(model):
        model = model.module
    # Model Summary
    with open(os.path.join(output_dir, f"model_summary{prefix}.log"), "a") as f:
        print(model, file=f)
        print(
            str(
                summary(
                    model,
                    input_size=input_size,
                    device=next(model.parameters()).device,
                    verbose=0,
                )
            ),
            file=f,
        )


def check_model_parallel(model):
    """check model is parallel or single

    Args:
        model (torch.nn.Module): Model file

    Returns:
        bool: parallel = True, single = False
    """
    return isinstance(model, torch.nn.DataParallel) or isinstance(model, DistributeDataParallel)
