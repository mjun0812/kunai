import logging
import subprocess
import sys
import os
import datetime
import csv
import re

import requests

logger = logging.getLogger()


def csv_to_list(path, head=False):
    """csv to 2D List

    Args:
        path (str): csv path
        head (bool, optional): Skip CSV header. Defaults to False.

    Returns:
        List: 2D List
    """
    with open(path, "r") as f:
        reader = csv.reader(f)
        if head:
            next(reader)
        data = [row for row in reader]
    return data


def get_cmd():
    """実行コマンドを取得する

    Returns:
        string: 実行コマンド

    Examples:
        get_cmd()
        -> python hoge.py --huga
    """
    cmd = "python " + " ".join(sys.argv)
    return cmd


def get_git_hash():
    """gitハッシュを取得する

    Returns:
        string: Gitのハッシュ値
    """
    cmd = "git rev-parse --short HEAD"
    try:
        git_hash = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT).strip().decode("utf-8")
    except Exception:
        git_hash = "Not found git repository"
    return git_hash


def post_slack(token, channel="#通知", username="通知", message=""):
    """slackにメッセージを送る. send slack message

    Args:
        token (str): Slack Token
        channel (str, optional): メッセージを送る通知先. Defaults to "#通知".
        username (str, optional): メッセージを送るユーザーの名前. Defaults to "通知".
        message (str, optional): send message. Defaults to "".

    Returns:
        int: http status code
    """
    response = requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Content-Type": "application/json"},
        params={
            "token": token,
            "channel": channel,
            "text": message,
            "username": username,
        },
    )
    return response.status_code


def setup_logger(rank, log_path):
    """loggerのセットアップをする
    ```python
    # write first on python script file
    import logging
    logger = logging.getLogger()

    # logging
    logger.info("test log")

    # output
    [2021-12-22 19:48:45,027][INFO] test log
    ```

    Args:
        rank (int): ログを記録するプロセスのランク．masterなら-1か0を設定．
        log_path (str): ログの保存先
    """
    # root loggerには最初からstremHandlerがある
    if rank in [-1, 0]:
        # MASTER RANK in DDP Mode or Single GPU Mode
        logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.INFO)
        logger.setLevel(logging.INFO)
        log_format = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
        file_handler = logging.FileHandler(log_path, "w")
        file_handler.setFormatter(log_format)
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        default_handler = logger.handlers[0]
        default_handler.setFormatter(log_format)
        default_handler.setLevel(logging.INFO)
    else:
        for h in logger.handlers[1:]:
            logger.removeHandler(h)
        # replica RANK in DDP Mode
        logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.ERROR)
        logger.setLevel(logging.ERROR)


def make_output_dirs(output_base_path: str, prefix="", child_dirs=None) -> str:
    """mkdir YYYYMMDD_HHmmSS (+ _prefix)

    Args:
        output_base_path (str): make output dir path.
        prefix (str, optional): add prefix mkdir. Defaults to "".
        child_dirs ([type], optional): mkdir child dir list. Defaults to None.

    Returns:
        str: YYYYMMDD_HHmmSS

    Examples:
    ```python
    out = make_output_dirs("./result", prefix="MODEL", child_dirs=["models", "figs"])

    ./result/21010812_120000
    ├── models
    └── figs
    ```
    """
    today = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    if prefix:
        prefix = "_" + prefix
    output_path = os.path.join(output_base_path, f"{today}{prefix}")
    os.makedirs(output_path, exist_ok=True)
    if child_dirs:
        for d in child_dirs:
            os.makedirs(os.path.join(output_path, d), exist_ok=True)
    return output_path


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r"(\d+)", text)]


def numerical_sort(list):
    """Numerical sort

    Args:
        list (list[str]): sort elements

    Returns:
        list: sorted list
    """
    return sorted(list, key=natural_keys)
