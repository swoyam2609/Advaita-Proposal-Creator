import fitz
from PIL import Image


def createPdf(input_pdf_path, output_pdf_path, image_path, x, y, width, height):

    pdf_document = fitz.open(input_pdf_path)

    img = Image.open(image_path)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save(image_path)

    image = pdf_document[0].insert_image(
        (x, y, x + width, y + height), filename=image_path)

    pdf_document.save(output_pdf_path)
    pdf_document.close()
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save(image_path)
