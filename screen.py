from mss import mss
from PIL import Image
import os
from datetime import datetime

def capture_screen():

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshots/{timestamp}.png"

    with mss() as sct:

        monitor = sct.monitors[1]

        screenshot =sct.grab(monitor)

        img = Image.frombytes(
            "RGB",
            screenshot.size,
            screenshot.rgb
        )
        print(f"Image Size:\n{img.width} x {img.height}")

        img.save(filename)

    return filename