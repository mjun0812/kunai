import logging
import os

from torchinfo import summary

import torch

logger = logging.getLogger()


def save_model(model, file_path):
    """save Pytorch Model

    Args:
        file_path (String): save file path
    """
    if check_model_parallel(model):
        model = model.module
    torch.save(model.state_dict(), file_path)
    logger.info("Saving model at %s", file_path)


def save_model_info(output_dir, model, input_size, prefix=""):
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
    return isinstance(model, torch.nn.DataParallel) or isinstance(model, torch.nn.parallel.DistributeDataParallel)
