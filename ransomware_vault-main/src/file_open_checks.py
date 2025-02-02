import PyPDF2
from PIL import Image
from docx import Document

from alarms import generate_alarm


def perform_image_open_check(filepath):
    try:
        Image.open(filepath)
        return True
    except:
        generate_alarm(filepath)
        return False


def perform_pdf_open_check(filepath):
    try:
        file = open(filepath, 'rb')
        PyPDF2.PdfFileReader(file)
        return True
    except:
        generate_alarm(filepath)
        return False


def perform_docx_open_check(filepath):
    try:
        Document(filepath)
        return True
    except:
        generate_alarm(filepath)
        return False


FILE_CHECK_FUNCTIONS = {
    "jpeg": perform_image_open_check,
    "jpg": perform_image_open_check,
    "png": perform_image_open_check,
    "pdf": perform_pdf_open_check,
    "docx": perform_docx_open_check,
}

FILE_FORMAT_MAPPING = {
    "jpeg": "jpeg",
    "jpg": "jpeg",
    "png": "png",
    "pdf": "pdf",
    "docx": "microsoft",
}