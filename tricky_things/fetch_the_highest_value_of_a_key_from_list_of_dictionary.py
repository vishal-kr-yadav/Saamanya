# find the highest value of a key among the list of dictionary
dummy_list_of_dict = [{'do': 0.3022559, 'malware': 0.040123496, u'denial': 0.099544674, 'request': 0.03568341, 'attacker': 0.042818766, 'full': 0.034019403},
      {'do': 0.2922559, 'malware': 0.040123496, u'denial': 0.099544674, 'request': 0.03568341, 'attacker': 0.042818766, 'full': 0.034019403}]

def main_function(keyword):

    result = max(xrange(len(dummy_list_of_dict)), key=lambda index: dummy_list_of_dict[index][keyword])
    return result


position_of_highest_dictionary_within_a_list=main_function("do")

print(dummy_list_of_dict[position_of_highest_dictionary_within_a_list])

# output:
# {'do': 0.3022559, 'malware': 0.040123496, u'denial': 0.099544674, 'request': 0.03568341, 'attacker': 0.042818766, 'full': 0.034019403}