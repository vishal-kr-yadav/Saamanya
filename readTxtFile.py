#!/usr/bin/python3
import os
import re

def getFileContent(rootDirPath):

    fileList = [item for item in os.listdir(rootDirPath) if os.path.isfile(os.path.join(rootDirPath, item))]
    filePathList =[]
    for eachFile in fileList:
        filePathList.append(rootDirPath+'/'+eachFile)
        # filePathList = ['/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-208-n1_v01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-191-n1_#01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-192-n1_f01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-193-n1_g01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-194-n1_h01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-195-n1_$01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-196-n1_j01!.TXT','/home/vishal/Desktop/HUDOC/HUDOC_TXT/001-197-n1_k01!.TXT']
    docComplete = []
    for filePath in filePathList:
        print(filePath)
        with open(filePath, 'r', encoding='utf16') as contentFile:
            content = contentFile.read()
            temp = (str(content)).replace('\n', ' ').replace('\t', ' ')
            # fileText = re.sub(r"[^a-zA-Z0-9]", " ", temp)
            print(temp)

            # docComplete.append(fileText)
    # return content

docTokens =getFileContent('/home/vishal/Desktop/HUDOC/test')
# print(docTokens)