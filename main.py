import pyttsx3
import PyPDF2

pdf_path = 'sample.pdf'
pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))
speaker = pyttsx3.init()
text_to_speak = ''  # To store all text from the PDF

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    text_to_speak += clean_text + ' '

speaker.save_to_file(text_to_speak, 'sample.mp3')
speaker.runAndWait()

speaker.stop()
