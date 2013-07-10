import os
import os.path

def py_files(dir_name):
    count = 0
    for content in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name,content)) and content.split(".")[-1] == "py":
            yield os.path.join(dir_name,content)

def line_count(filenames):
    count=0
    for f in filenames:
        for line in open(f):
            if line[0] != '#' and line[0] != '\n':
                count+=1
    return count

def py_loc2(dir_name):
    file_list=py_files(dir_name)
    count=count_lst(file_list)
    return count
