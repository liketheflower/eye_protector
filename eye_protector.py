from PIL import Image
import time

TIME_PERIOD = 60 * 20  # 20 minutes
TEST = True
if TEST:
    TIME_PERIOD = 10  # wait only 10 seconds to have a quick test


def img_reminding():
    im = Image.open("img1.png")
    im.show()
    time.sleep(4)
    im = Image.open("img2.png")
    im.show()


def eye_protector():
    while True:
        time.sleep(TIME_PERIOD)
        img_reminding()


if __name__ == "__main__":
    eye_protector()
