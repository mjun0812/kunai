import logging
import os

import yaml
from omegaconf import OmegaConf


logger = logging.getLogger()


def is_available(func):
    def wrapper(*args, **kwargs):
        global hydra
        try:
            import hydra

            return func(*args, **kwargs)
        except (ImportError, TypeError):
            print("Please install hydra `pip install hydra-core`")
            return

    return wrapper


@is_available
def set_hydra(cfg, verbose=True):
    """configファイルを標準出力し，Current Dirを実行スクリプトの場所に戻す．

    hydraは使用時にカレントディレクトリを変更するため，
    hydra.utils.get_original_cwdを使って実行ディレクトリを取得して
    もとに戻す．

    Args:
        cfg (OmegaConf.omegaconf): Hydra config obj.
    """
    if verbose:
        # Print config
        print(OmegaConf.to_yaml(cfg))
    # Hydraはcurrent directryを実行場所から変更するのでもとに戻しておく
    os.chdir(hydra.utils.get_original_cwd())


def get_default_config(config_dir_path, config_name="config.yaml"):
    """hydraを使わずにディレクトリに分割されたyamlの設定ファイルをOmegaConfに変換する

    ２つ以上の設定ファイルを比較するときに必要

    Args:
        config_dir_path (str): config群があるディレクトリ
        config_name (str, optional): configのファイル名. Defaults to "config.yaml".

    Returns:
        OmegaConf.omegaconf: omegaconf
    """
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
    """2つのOmegaConfをマージする．

    main関数でロードしたものと，デフォルトで使っているものをマージする．
    開発中にデフォルトのconfigに追加があった場合に，既に生成されたconfigに
    追加した項目をロードしたconfigに追加するために使う

    ```yaml
    # load config
    HOGE: 3

    # default config
    HOGE: 2
    HUGA: 1

    # merged config
    HOGE: 3
    HUGA: 1
    ```

    Args:
        cfg (OmegaConf.omegaconf): ロードしたconfigファイル

    Returns:
        OmegaConf.omegaconf: マージされたconfigファイル
    """
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
    """dictのkeyを再帰的に列挙したリストを取得する

    Args:
        base (dict): 列挙するリスト
        base_name (str, optional): 親の階層のkey．再起実行用. Defaults to "".

    Returns:
        list: dictのkeyのリスト
    """
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
