from pdf2docx import Converter
import glob  # check things in current directory

for pdf_file in glob.glob("*.pdf"):
    cv = Converter(pdf_file)
    cv.convert(pdf_file.replace("pdf", "docx"))
    cv.close()
