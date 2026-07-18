import easyocr

reader = easyocr.Reader(['en'])


def read_text_from_image(image_path):
    results = reader.readtext(image_path)

    extracted_text = []

    for result in results:
        extracted_text.append(result[1])

    return "\n".join(extracted_text)