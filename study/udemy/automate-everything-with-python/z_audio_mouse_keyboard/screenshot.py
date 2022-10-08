from datetime import datetime
from pathlib import Path
from typing import Optional

from mss import mss, tools

from z_audio_mouse_keyboard.constants import TEMP_FOLDER_PATH


def capture_full_screenshot(output_path: Optional[Path] = None):
    output_path = output_path or TEMP_FOLDER_PATH.joinpath(
        f"full_screenshot_{datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S.%z')}.png"
    )

    with mss() as sct:
        try:
            # Only works in Xorg - X11 Windows Systems
            filename = sct.shot(output=output_path.as_posix())
            print(filename)
        except Exception as err:
            print(f"!!!ERROR!!! {err}")


def capture_screenshot(
    top: int = 0,
    left: int = 0,
    width: int = 500,
    height: int = 400,
    output_path: Optional[Path] = None,
):
    output_path = output_path or TEMP_FOLDER_PATH.joinpath(
        f"full_screenshot_{datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S.%z')}.png"
    )

    with mss() as sct:
        try:
            # Only works in Xorg - X11 Windows Systems
            image = sct.grab(
                {"top": top, "left": left, "width": width, "height": height}
            )
            tools.to_png(image.rgb, image.size, output=output_path)
        except Exception as err:
            print(f"!!!ERROR!!! {err}")


def main():
    capture_full_screenshot()
    capture_screenshot()


if __name__ == "__main__":
    main()
