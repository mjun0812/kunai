import logging
import os

from torchinfo import summary

import torch

logger = logging.getLogger()


def save_model(model, file_path, multi_gpu):
    """save Pytorch Model

    Args:
        file_path (String): save file path
    """
    if multi_gpu:
        model = model.module
    torch.save(model.state_dict(), file_path)
    logger.info("Saving model at %s", file_path)


def save_model_info(output_dir, model, input_size, prefix=""):
    if prefix:
        prefix = "_" + prefix
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
