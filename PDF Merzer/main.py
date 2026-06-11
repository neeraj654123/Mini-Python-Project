from PyPDF2 import PdfMerger

merger = PdfMerger()
pdfs = []

n = int(input("How many PDFs do you want to merge: "))

for i in range(n):
    name = input(f"Enter name of  {i + 1} pdf: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

print("Merging completed! Saved as merged-pdf.pdf")
