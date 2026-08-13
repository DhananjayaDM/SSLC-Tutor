import fitz
import io
import os
import json

from PIL import (
    Image,
    ImageFilter,
    ImageOps
)

from rapidocr_onnxruntime import RapidOCR


ocr = RapidOCR()


def save_pages(pdf_path):

    doc = fitz.open(pdf_path)

    os.makedirs(
        "data/pages",
        exist_ok=True
    )

    for page_num in range(len(doc)):

        page = doc[page_num]

        pix = page.get_pixmap(
            dpi=500
        )

        output_path = (
            f"data/pages/page_{page_num + 1}.png"
        )

        pix.save(output_path)

        print(
            f"Saved: {output_path}"
        )

    doc.close()


def preprocess_image(image):

    image = image.convert("L")

    image = ImageOps.autocontrast(
        image
    )

    image = image.resize(
        (
            image.width * 2,
            image.height * 2
        ),
        Image.Resampling.LANCZOS
    )

    image = image.filter(
        ImageFilter.SHARPEN
    )

    image = image.filter(
        ImageFilter.MedianFilter(3)
    )

    image = image.point(
        lambda x: 255 if x > 150 else 0
    )

    return image


def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    os.makedirs(
        "data/cache",
        exist_ok=True
    )

    full_text = []

    page_data = []

    for page_no, page in enumerate(
        doc,
        start=1
    ):

        print(
            f"Reading Page {page_no}"
        )

        pix = page.get_pixmap(
            dpi=500
        )

        img_bytes = pix.tobytes(
            "png"
        )

        image = Image.open(
            io.BytesIO(img_bytes)
        )

        image = preprocess_image(
            image
        )

        result, _ = ocr(image)

        page_text = ""

        if result:

            try:

                page_text = "\n".join(
                    item[1]
                    for item in result
                )

            except Exception:

                page_text = "\n".join(
                    str(item)
                    for item in result
                )

            full_text.append(
                page_text
            )

        page_data.append(
            {
                "page": page_no,
                "content": page_text
            }
        )

    doc.close()

    with open(
        "data/cache/page_text.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            page_data,
            f,
            indent=4,
            ensure_ascii=False
        )

    full_text_content = "\n".join(
        full_text
    )

    with open(
        "data/cache/full_text.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            full_text_content
        )

    print(
        "Saved OCR cache:"
        " data/cache/page_text.json"
    )

    return full_text_content