import os


def get_pat_of_file(path):
    main_dir=path
    list_of_sub_dir= [path for path in os.listdir(main_dir) if os.path.isdir(main_dir)]

    temp_list=[]
    final_list_of_file=[]
    for each in list_of_sub_dir:
        path_of_sub_dr = os.path.join(main_dir, each)
        temp_list.append(path_of_sub_dr)

    for each in temp_list:
        a=os.listdir(each)
        for each1 in a:
            final_list_of_file.append(os.path.join(each, each1))
    return final_list_of_file
print(get_pat_of_file("/home/vishal/Desktop/malware_type"))

# it will works, if your directory structure is as below
# +main_dir
#     +sub_dir
#         -file1
#     +sub_dir2
#         -file2
