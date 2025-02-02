import pytest

from main import check_file_type, verify_file_type_without_extension, perform_file_security_check


@pytest.mark.parametrize("filename, result", [
    ("something.pdf", ".pdf"),
    ("something_pdf.jpg", ".jpg"),
    ("som/eth/ing_pdf.jpg", ".jpg"),
    ("/something_pdf.jpg", ".jpg"),
    ("test/something_pdf.jpg", ".jpg"),
])
def test_check_file_type(filename, result):
    assert check_file_type(filename) == result


@pytest.mark.parametrize("filename, file_extension, result", [
    ("sample_files/sample.pdf", "pdf", True),
    ("sample_files/sample_png.pdf", "pdf", False),
    ("sample_files/sample_txt.pdf", "pdf", False),
    ("sample_files/sample_pdf.jpg", "jpg", False),
])
def test_verify_file_type_without_extension(filename, file_extension, result):
    assert verify_file_type_without_extension(filename, file_extension, activate_alarm=False) == result


@pytest.mark.parametrize("filename, file_extension, result", [
    ("sample_files/sample.jpg", "jpg", None),
    ("sample_files/sample.jpeg", "jpeg", None),
    ("sample_files/sample.png", "png", None),
    ("sample_files/sample.docx", "docx", None),
    ("sample_files/sample.pdf", "pdf", None),
])
def test_perform_file_security_check(filename, file_extension, result):
    assert perform_file_security_check(filename, file_extension) == result