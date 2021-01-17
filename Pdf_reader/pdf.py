import PyPDF2

# Write the name of the pdf and if which color format you want to load it to the memory
with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	print(reader.numPages)
