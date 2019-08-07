import json
# read file
def readJson(fileName):
    with open(fileName, 'r') as myfile:
        topicsData=myfile.read()

    #If you have a JSON string, you can parse it by using the json.loads() method.
    topics = json.loads(topicsData)
    return topics

jsonData =readJson('topic.json')


with open('sample.json', 'w') as outfile:
    json.dump(word2VecOutput, outfile)