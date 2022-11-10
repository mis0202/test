from PyPDF2 import PdfFileReader as reader
from gtts import gTTS


def create_audio(pdf_file):
    read_Pdf = reader(open(pdf_file, 'rb'))
    for page in range(read_Pdf.numPages):
        text = read_Pdf.getPage(page).extractText()
        tts = gTTS(text, lang='en')
        tts.save('page' + str(page) + '.mp3')


create_audio('一次k8s未正常启动的排查-etcd文件损坏.pdf')