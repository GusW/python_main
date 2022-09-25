from l_image_processing.constants import EX_01_IMAGES_PATH, EX_02_RESIZEDIMAGES_PATH
from l_image_processing.resize_image import resize_image


def main():
    for image_path in EX_01_IMAGES_PATH.iterdir():
        resize_image(image_path, 35, EX_02_RESIZEDIMAGES_PATH)


if __name__ == "__main__":
    main()
