# coding: utf-8

import os
import time
from PIL import Image

LEN = 78
SIZE = (78, 36)


def resize_img():
    """resize images
    """
    lst = get_files("jpeg")
    for x in lst:
        img = Image.open(x)
        out = img.resize(SIZE)
        out.save(x[:-4] + "jpg")

    os.system("rm *.jpeg")


def get_files(suffix):
    """get files by suffix
    """
    lst = os.listdir(".")
    return filter(lambda x: x.endswith(suffix), lst)


def gen_char_img(data, t_name):
    """generate char image
    """
    position = 1
    with open(t_name, "w") as f:
        for x, y, z in data:
            if position > LEN :
                f.write("\n")
                position = 1
            # char style
            f.write(char_style(x, y, z))
            position += 1

    os.system("rm " + t_name[:-3] + "jpg")
    print t_name, " done ..."

def char_style(x, y, z):
    """char style
    """
    if x > 155: return " "
    elif y > 155: return "%"
    elif z > 155: return "@"

    return "*"

def main():
    resize_img()
    lst = get_files("jpg")
    for f in lst:
        img = Image.open(f)
        r = img.getdata()
        gen_char_img(r, f[:-3] + "txt")


if __name__ == "__main__":
    main()
