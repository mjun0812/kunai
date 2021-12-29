import logging
import os

import yaml
from omegaconf import OmegaConf

import hydra

logger = logging.getLogger()


def set_hydra(cfg):
    # Print config
    print(OmegaConf.to_yaml(cfg))
    # Hydraはcurrent directryを実行場所から変更するのでもとに戻しておく
    os.chdir(hydra.utils.get_original_cwd())


def get_default_config(config_dir_path, config_name="config.yaml"):
    # get default root config
    with open(os.path.join(config_dir_path, config_name), "r") as f:
        cfg = yaml.safe_load(f)
    default = {}
    for d in cfg["defaults"]:
        try:
            default.update(d)
        except Exception:
            pass

    # get nest config key
    file_list = os.listdir(config_dir_path)
    dir_list = [f for f in file_list if os.path.isdir(os.path.join(config_dir_path, f))]

    for dir_name in dir_list:
        cfg_name = default[dir_name]
        with open(os.path.join(config_dir_path, dir_name, cfg_name + ".yaml")) as f:
            split_cfg = yaml.safe_load(f)
        cfg[dir_name] = split_cfg
    cfg = OmegaConf.create(cfg)

    return cfg


def validate_config(cfg):
    default_cfg = get_default_config("./config")
    default_keys = enum_dict_keys(OmegaConf.to_container(default_cfg, resolve=True))
    cfg_keys = enum_dict_keys(OmegaConf.to_container(cfg, resolve=True))
    if set(default_keys) - set(cfg_keys):
        logger.warning(f"input config nothing keys: {set(default_keys) - set(cfg_keys)}")
    if set(cfg_keys) - set(default_keys):
        logger.warning(f"not using keys input config: {set(cfg_keys) - set(default_keys)}")

    merge = OmegaConf.merge(default_cfg, cfg)
    return merge


def enum_dict_keys(base, base_name=""):
    key_list = []
    for key in base.keys():
        if base_name:
            key_name = base_name + "." + key
        else:
            key_name = key
        if isinstance(base[key], dict):
            key_list.extend(enum_dict_keys(base[key], base_name=key_name))
        else:
            key_list.append(key_name)
    return key_list
