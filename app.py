from screen import capture_screen
from ocr import read_text_from_image
from ai import ask_ai

def main():
    print("Capturing screen...")

    path = capture_screen()

    print("✔ Screenshot saved successfully! \n Location: \n", path)
    text = read_text_from_image(path)
    print(text)

    if not text.strip():
        print("\nNo text detected.")
        return

    print("\nThinking...\n")

    prompt = f"""
You are a helpful AI tutor.

Explain the following text in simple words.

{text}
"""

    answer = ask_ai(prompt)

    print("AI Response:")
    print("-" * 50)
    print(answer)


if __name__ == "__main__":
    main()