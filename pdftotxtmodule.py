from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os

def convert_pdf_to_txt(path, output):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'ascii'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    
    foutput = open(output, 'w')
    foutput.write(str)
    return str

DIR_pdfs = 'pdfs/'
DIR_corpus = 'corpus/'

for pdf_file in os.listdir(DIR_pdfs):
    convert_pdf_to_txt(DIR_pdfs+pdf_file, DIR_corpus+pdf_file.replace(".pdf", ".txt"))
    print "pdf"+pdf_file+" has been converted"

print "Done."


