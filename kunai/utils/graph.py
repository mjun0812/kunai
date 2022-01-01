import os
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


def draw_image_graph(images, captions, filename, row, col, all_title="", dpi=150):
    """matplotlibで画像を並べたグラフを保存する

    Args:
        images (list[np.ndarray]): 画像のリスト
        captions (list[str]): 各画像につけるキャプションのリスト
        filename (str): 図を保存するPath
        row (int): 行
        col (int): 列
        all_title (str, optional): 図全体のキャプション. Defaults to "".
        dpi (int, optional): 保存する図のDPI. Defaults to 150.
    """

    plt.gcf().clear()

    # 論文用にFontを変更する
    if os.path.exists("./etc/Times_New_Roman.ttf"):
        font_manager.fontManager.addfont("./etc/Times_New_Roman.ttf")
        plt.rcParams.update(
            {
                "font.family": "Times New Roman",
                "font.size": 18,
                # "text.usetex": True,
                "ps.useafm": True,
                "pdf.use14corefonts": True,
            }
        )

    # 比率が合わないときはfigsizeをいじる
    fig, axs = plt.subplots(row, col, figsize=(col * 2, row * 2))
    plt.subplots_adjust(wspace=0.1, hspace=0.1)
    # 1次元にしてforで回せるように。行->列の順
    a = axs.ravel()
    for i in range(len(images)):
        a[i].imshow(images[i])
        a[i].axis("off")
        a[i].set_title(captions[i], y=-0.06 * col, fontsize=7)  # 下にキャプション
        # a[i].set_title(captions[i], fontsize=7)  # 上にキャプション
    # 全体のタイトル
    if all_title:
        fig.suptitle(all_title, fontsize=5)
        fig.tight_layout(rect=[0, 0, 1, 0.98])

    # DPIがでかすぎるとファイルサイズも大きくなり、プログラムの速度も落ちる
    # DPI * figsizeの解像度の画像ができる
    plt.savefig(filename, dpi=dpi, bbox_inches="tight")
    plt.gcf().clear()
    plt.close()


def fig_to_numpy(fig):
    """Matplotlibのfigureをnumpy arrayに変換

    Args:
        fig (fig): MatplotlibのFigure

    Returns:
        numpy.ndarray: 画像
    """
    fig.canvas.draw()
    return np.array(fig.canvas.renderer.buffer_rgba())
