# take no. of input
# loop n no of times and take input
# print(result)

n = int(input().strip())
phonebook = {}
for i in range(n):
    line = input()
    k, v = line.split()
    phonebook[k] = v

while True:
    try:
        number = input()
    except EOFError:
        break
    if number in phonebook:
        print("{}={}".format(number, phonebook[number]))
    else:
        print("Not found")

#
# Sample Input
#
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
#
# Sample Output
#
# sam=99912222
# Not found
# harry=12299933
