from screen import capture_screen
from ocr import read_text_from_image
print("Capturing screen...")

path = capture_screen()

print("✔ Screenshot saved successfully! \n Location: \n", path)
text = read_text_from_image(path)
print(text)
