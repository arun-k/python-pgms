import os
import os.path

def py_files(dir_name):
    count = 0
    for content in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name,content)) and content.split(".")[-1] == "py":
            yield os.path.join(dir_name,content)

def count_lst(filenames):
    for fil in filenames:
        f=open(fil,'r')
        yield len(f.readlines())
        f.close()

def py_loc(dir_name):
    file_list=py_files(dir_name)
    count=count_lst(file_list)
    return sum(count)

        
