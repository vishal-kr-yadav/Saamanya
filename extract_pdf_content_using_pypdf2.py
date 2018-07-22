# importing required modules
import test111
import PyPDF2
import unicodedata


# pdfFileName=test111.one()
# print("==============",pdfFileName)

def remove_non_ascii_1(text):
    return ''.join([i if ord(i) < 128 else ' ' for i in text])

# creating a pdf file object
pdfFileObj = open('/home/vishal/Desktop/malware_type/CyberAsk Adware/Adware & Cryptomining Remain Top Enterprise Security Threats - Security Now.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
page_number=pdfReader.numPagese
print(page_number)

i=0
f = open('/home/vishal/merlin/cyber_ask/data/3viruses.txt', 'a')
while i<page_number:
    # creating a page object
    pageObj = pdfReader.getPage(i)

    # extracting text from page
    # print((pageObj.extractText()))

    f.write(remove_non_ascii_1(pageObj.extractText()))
    # f.write(unicodedata.normalize('NFKD', remove_non_ascii_1(pageObj.extractText())).encode('ascii','ignore'))
    f.write("\n")
    # f.write("\n")

    i += 1
f.close()

# closing the pdf file object
pdfFileObj.close()

#
# extract pdf file using pypdf and write into a .txt file
# it will work from pdf doc but not for all
# pdfminer is better than this

