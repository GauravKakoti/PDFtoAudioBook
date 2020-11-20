#Description: This program converts a PDF to a audio book
import pyttsx3
import pdfplumber
import PyPDF2

#Get the file name and the location of the PDF file
file = 'Steve_Nison-Japanese_Candlestick_Charting_Techniques-EN.pdf'

#Create a PDF file object
pdfFileObj = open(file, 'rb')

#Create a PDF File Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Get the no. of pages
pages = pdfReader.numPages

#Create a pdfplumber object and loop through the number of pages in PDF file
with pdfplumber.open(file) as pdf:
    #Loop through the number of pages
    for i in range(15, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()