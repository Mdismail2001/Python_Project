from PyPDF2 import PdfMerger
ALLPDF = ["Document.pdf","2.PDF.pdf"]

merger = PdfMerger()

for pdf in ALLPDF:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
