from zc_miscellaneous.constants import TEMP_FOLDER_PATH
from zc_miscellaneous.qr_code import create_qr_code


def main():
    with open(TEMP_FOLDER_PATH.joinpath("urls.txt"), mode="r") as file_:
        urls = file_.read().split()
        create_qr_code(urls, TEMP_FOLDER_PATH)


if __name__ == "__main__":
    main()
