from pathlib import Path
import qrcode
import webbrowser

from cv2 import (
    VideoCapture,
    QRCodeDetector,
    imshow,
    imread,
    waitKey,
    destroyAllWindows,
)


from zc_miscellaneous.constants import TEMP_FOLDER_PATH


def extract_from_image(file_path: Path) -> dict[str, str]:
    detector = QRCodeDetector()
    image = imread(file_path.as_posix())

    url, coordinates, pixels = detector.detectAndDecode(image)
    return {"url": url, "coordinates": coordinates, "pixels": pixels}


def open_url_from_qr_data(qr_data: dict[str, str]) -> None:
    if qr_data and (url := qr_data.get("url")):
        webbrowser.open(url)


def extract_from_camera():
    video = VideoCapture(0)  # int 0: main device camera; 1, 2...
    success, frame = video.read()
    detector = QRCodeDetector()

    def _close_camera():
        video.release()
        destroyAllWindows()

    while True:
        url, coordinates, pixels = detector.detectAndDecode(frame)
        if url:
            _close_camera()
            return {"url": url, "coordinates": coordinates, "pixels": pixels}

        success, frame = video.read()
        if not success:
            break

        # visual feedback
        imshow("Place QR code into camera frame...", frame)

        if (key := waitKey(1)) and key == ord("q"):
            break

    _close_camera()


def create_qr_code(urls: list[str], destination_folder: Path):
    for idx, url in enumerate(urls):
        try:
            qr_code = qrcode.make(url)
            qr_code.save(destination_folder.joinpath(f"{idx}.png"))
        except Exception as err:
            print(f"!!!ERROR!!! Could not create QR for {url}: {err}")


def main() -> None:
    file_path = Path.joinpath(TEMP_FOLDER_PATH, "qr.png")
    qr_data = extract_from_image(file_path)
    print(f"{qr_data=}")
    open_url_from_qr_data(qr_data)

    qr_data_live = extract_from_camera()
    open_url_from_qr_data(qr_data_live)

    urls = ["www.google.com", "www.cnn.com"]
    create_qr_code(urls, TEMP_FOLDER_PATH)


if __name__ == "__main__":
    main()
