def alternatingCharacters(s):
    # t = input()
    # for _ in range(t):
    #     s = raw_input()
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
        print(count)


alternatingCharacters('AAAAB')

# a= [1,2,3]
# for each in range(0,len(a)-1):
#     print(len(a))
#     del a[each]
    # print(each)

    # print(len(a))
    # break
