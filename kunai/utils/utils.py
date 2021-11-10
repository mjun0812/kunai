import subprocess
import sys

import requests


def get_cmd():
    """実行コマンドを取得する"""
    cmd = "python " + " ".join(sys.argv)
    return cmd


def get_git_hash():
    """gitハッシュを取得する

    Returns:
        string: Gitのハッシュ値
    """
    cmd = "git rev-parse --short HEAD"
    git_hash = subprocess.check_output(cmd.split()).strip().decode("utf-8")
    return git_hash


def post_slack(token, channel="#通知", username="通知", message=""):
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
