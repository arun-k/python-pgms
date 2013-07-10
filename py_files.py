import os
import os.path

def py_files(dir_name):
    count = 0
    for content in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name,content)) and content.split(".")[-1] == "py":
            count+=1
    return count
        
        
