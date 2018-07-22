from __future__ import print_function
import io ,os
def remove_non_ascii(fileName):
    writeFile=fileName.split('/')[-1]
    nonascii = bytearray(range(0x80, 0x100))
    with open(fileName,'rb') as infile, open("/home/vishal/merlin/cyber_ask/data1/"+writeFile,'wb') as outfile:
        for line in infile: # b'\n'-separated lines (Linux, OSX, Windows)
            outfile.write(line.translate(None, nonascii))


# remove_non_ascii('/home/vishal/merlin/cyber_ask/data2/10.txt')
def dir_name(dir_name):
    a=os.listdir(dir_name)
    # print(len(a))
    for each in a:
        # print("===","/home/vishal/merlin/cyber_ask/data1/"+each)
        remove_non_ascii("/home/vishal/merlin/cyber_ask/data/"+each)



dir_name("/home/vishal/merlin/cyber_ask/data")
