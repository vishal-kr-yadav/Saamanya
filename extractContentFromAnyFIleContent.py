#This script can extract text from a
#ref : https://textract.readthedocs.io/en/stable/
import textract

def extractDocContent(rootDir, eachFile):
    filePath = rootDir+eachFile
    text = textract.process(filePath).decode("utf-8").replace("\n", "").replace("\\n", "").replace("\\","")
    return text


# rootDir ="/home/vishal/Desktop/"
rootDir ="/home/vishal/test_cse/dataExtractionLFS/sampleDir/pdfFIles/"


listOfFiles = ["1569614492875_RHQCC19074.pdf"]
for eachFile in listOfFiles:
    extractDocContent(rootDir, eachFile)