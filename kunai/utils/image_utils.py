import os

import cv2


def image_viewer(image_list):
    """OpenCV Base Image Viewer

        Next Image: key m, d, right key
        Previous Image: key n, a, left key
        Quit: q

    Args:
        image_list (list[str]): Image path list
    """
    # Set keycodes for changing images
    # 81, 83 are left and right arrows on linux in Ascii code
    # (probably not needed)
    # 65361, 65363 are left and right arrows in linux
    # 2424832, 2555904 are left and right arrows on Windows
    # 110, 109 are 'n' and 'm' on mac, windows, linux
    # (unfortunately arrow keys not picked up on mac)
    leftkeys = (81, 110, 97, 65361, 2424832)
    rightkeys = (83, 109, 100, 65363, 2555904)

    i = 0
    cv2.namedWindow("Image", cv2.WINDOW_GUI_EXPANDED | cv2.WINDOW_NORMAL)

    while True:
        image_path = image_list[i]
        image = cv2.imread(image_path)

        cv2.imshow("Image", image)

        print(f"{os.path.basename(image_path)}  ({i + 1}/{len(image_list)})")

        key = cv2.waitKeyEx()
        if (key == ord("d")) or key in rightkeys:
            i += 1
            if i >= len(image_list):
                i = 0
        if (key == ord("a")) or key in leftkeys:
            i -= 1
            if i < 0:
                i = len(image_list) - 1
        if (key == ord("q")) or (key == 27):
            break
