topic_word_distribution_list=[{u'spread': 0.036251955, u'virus': 0.31319818, u'code': 0.041378938, u'worm': 0.11132102, u'file': 0.04207533}]

def to_utf8(topic_word_distribution_list):
    final = []
    for item in topic_word_distribution_list:
        if type(item) is dict:
            result = {}
            for key, value in item.items():
                result[str(key)] = str(value)
            final.append(result)
    return final

print ("Before removing the unicode : ",topic_word_distribution_list)
print ("After removing the unicode : ",to_utf8(topic_word_distribution_list))