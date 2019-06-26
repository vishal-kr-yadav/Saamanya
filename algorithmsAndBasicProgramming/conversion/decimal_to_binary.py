def decimal_to_binary(decimal_number):
    global_list = []
    while decimal_number > 0:

        remainder =  decimal_number % 2
        decimal_number = decimal_number // 2

        global_list.append(remainder)

    return global_list
# print(decimal_to_binary(5))

def find_the_consecutive_one(list_of_element):
    result = 0
    count = 0
    for each_element in range(0,len(list_of_element)):

        if list_of_element[each_element] == 0 :

            count = 0
        else :
            count+= 1
            result = max(result,count)

    return result



print(find_the_consecutive_one([1,1,0,1]))