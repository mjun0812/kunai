import logging
import os
from pprint import pprint

logger = logging.getLogger()


def is_available(func):
    def wrapper(*args, **kwargs):
        global torch, summary, DistributedDataParallel
        try:
            import torch
            from torch.nn.parallel import DistributedDataParallel
            from torchinfo import summary

            return func(*args, **kwargs)
        except (ImportError, TypeError):
            print("Please install torch, torchinfo `pip install torch torchinfo`")
            return

    return wrapper


@is_available
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


@is_available
def save_model_info(output_dir, model, input_size=None, input_data=None, prefix=""):
    """Output PyTorch Model Summary to log.

    Args:
        output_dir (string): output log dir
        model (torch.nn.Module): PyTorch Model Class
        input_size (List): input tensor size
        input_data (List[Tensor]): input data
        prefix (str, optional): log file prefix output_dir/model_summary_{prefix}.log. Defaults to "".
    """

    if prefix:
        prefix = "_" + prefix
    if check_model_parallel(model):
        model = model.module

    device = next(model.parameters()).device

    if input_size is None:
        model_summary = str(summary(model, input_data=input_data, device=device, verbose=0))
    elif input_data is None:
        model_summary = str(summary(model, input_size=input_size, device=device, verbose=0))
    else:
        model_summary = str(summary(model, device=device, verbose=0))

    # Model Summary
    with open(os.path.join(output_dir, f"model_summary{prefix}.log"), "a") as f:
        print(model, file=f)
        print(model_summary, file=f)


@is_available
def check_model_parallel(model) -> bool:
    """check model is parallel or single

    Args:
        model (torch.nn.Module): Model file

    Returns:
        bool: parallel = True, single = False
    """
    return isinstance(model, torch.nn.DataParallel) or isinstance(model, DistributedDataParallel)

@is_available
def calc_params(params_dict: dict) -> int:
    """Calculate number of parameters

    Args:
        params_dict (dict): PyTorch model state_dict

    Returns:
        int: num params
    """
    num_params = 0
    for v in params_dict.values():
        n = 1
        for p in v.shape:
            n *= p
        num_params += n
    return num_params

@is_available
def prety_print_model_param(state_dict: dict) -> None:
    """Print model parameters

    Args:
        state_dict (dict): PyTorch model state_dict
    """
    parsed_dict = {}
    for key, param in state_dict.items():
        keys = key.split(".")

        tmp_dict = parsed_dict
        for k in keys[:-1]:
            tmp_dict[k] = tmp_dict.get(k, {})
            tmp_dict = tmp_dict[k]
        num_params = 0
        for p in param.shape:
            num_params *= p
        tmp_dict[keys[-1]] = f"{list(param.shape)} {num_params}"
    pprint(parsed_dict)