import os
import tkinter
import time
from tkinter import filedialog
import threading
path=filedialog.askdirectory()
l=os.listdir(path)
def pdflist(s):
    if s.endswith(".pdf"):
        return s
l=list(filter(pdflist,l))
def encrypter(x):
    print(x)
    pdfReader=PyPDF2.PdfFileReader(x,"rb")
    pdfWriter=PyPDF2.PdfFileWriter()
    for pn in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pn))
    pdfWriter.encrypt('test123')
    res=open(x +'_encrypted.pdf','wb')
    pdfWriter.write(res)
    res.close()
    print("successfully encrypted at"+ time.ctime())
for i in l:
    t=threading.Thread(target=encrypter,args=[path+'/' +i,])
    t.start()
    t.join()

