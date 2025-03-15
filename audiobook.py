import PyPDF2
import pyttsx3

Engine= pyttsx3.init()
PDF_Reader= PyPDF2.PdfFileReader(open("What is python.pdf","rb"))
for Page_num in range(PDF_Reader.numPages):
    Text= PDF_Reader.getPage(Page_num).extractText()
    Engine.say(Text)
    Engine.runandWait()
    #Engine.save_to_file(Text,"audio.mp3") to save the file as an audio
    #Engine.runandwait() to wait until the speech is completed
