import pdftotext
with open("StarHealth1.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
details = pdf[1]

with open("tb.txt", "w",encoding="utf-8") as f:
    f.write(details)