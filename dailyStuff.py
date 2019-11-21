import collections

import itertools

# count the frequency of each word from the list of elements
topic = ["ab","ab","bcd","bcde","bcd"]
countElements = collections.Counter(topic)

frequencyofElements = dict(countElements)
print("result====",frequencyofElements)


#Get the first N elements from the
result = dict(itertools.islice(frequencyofElements.items(), 2))
print("result====",result)
