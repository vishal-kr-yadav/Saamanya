from tika import parser
import ast

def extractPdfContent(rootDir, eachFile):

    filePath = rootDir + eachFile
    raw = parser.from_file(filePath)
    raw = str(raw)
    safe_text = str(raw).replace("\n", "").replace("\\n", "").replace("\\","")

    #convert string to dictionary
    dict_text = ast.literal_eval(safe_text)

    #Get Keys of file
    allKeys = dict_text.keys()
    content = dict_text['content']
    status = dict_text['status']
    metadata = dict_text['metadata']

    return status,metadata

# rootDir ="/home/vishal/Desktop/"
rootDir ="/home/vishal/test_cse/dataExtractionLFS/sampleDir/pdfFIles/"


listOfFiles = ["1569614492875_RHQCC19074.pdf"]
for eachFile in listOfFiles:
    extractPdfContent(rootDir, eachFile)



