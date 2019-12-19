from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os


def extractContentOCR(Scan_PDF_File):
    pages = convert_from_path(Scan_PDF_File, 500)

    for page in pages:
        content = str(((pytesseract.image_to_string(page)))).replace('-\n', '')

        return content


Scan_PDF_File = "scansmpl.pdf"
print(extractContentOCR(Scan_PDF_File))

