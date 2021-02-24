from PIL import Image
import time

TIME_PERIOD_SECOND = 60 * 20  # 20 minutes
QUICK_TEST = True
if QUICK_TEST:
    TIME_PERIOD_SECOND = 10  # wait only 10 seconds to have a quick test


def read_img_and_show(img_name):
    im = Image.open(img_name)
    im.show()


def img_reminding():
    read_img_and_show("./../imgs/img1.png")
    time.sleep(4)
    read_img_and_show("./../imgs/img2.png")


def eye_protector():
    while True:
        time.sleep(TIME_PERIOD_SECOND)
        img_reminding()


if __name__ == "__main__":
    eye_protector()
