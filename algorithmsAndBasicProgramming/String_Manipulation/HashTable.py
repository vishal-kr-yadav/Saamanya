def checkMagazine(magazine, note):
    from collections import Counter

    result = (Counter(note) - Counter(magazine)) == {}
    print(result)
    # counter=0
    # for each_note in note:
    #
    #     if each_note in magazine:
    #         magazine.remove(each_note)
    #         counter+=1
    # print(counter)
    # print(len(note))
    # if len(note) == counter:
    #
    #
    #     print("Yes")
    # else:
    #
    #     print("No")
# # >>> a = [10, 20, 30, 40, 20, 30, 40, 20, 70, 20]
# # >>> a = [x for x in a if x != 20]
# # >>> print a
#
a=['give', 'me', 'one', 'grand', 'today', 'night']
b=['give', 'me', 'one', 'grand', 'today', 'night']


checkMagazine(a, b)
# magazine = input().rstrip().split()
# note = input().rstrip().split()
# checkMagazine(magazine, note)