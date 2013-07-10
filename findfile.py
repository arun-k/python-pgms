import os
import os.path

def search_tree(dir_name):
    base_paths=[]
    for content in os.listdir(dir_name):
        if os.path.isdir(os.path.join(dir_name,content)):
            base_paths+=(search_tree(os.path.join(dir_name,content)))
        else:
            base_paths.append(os.path.join(dir_name,content))
    return base_paths

def full_paths(pathlist):
    for path in pathlist:
        yield os.path.abspath(path)
        
def printpaths(paths):
    for path in paths:
        print path

def findfiles(dirname):
    base_paths=search_tree(dirname)
    abs_paths=full_paths(base_paths)
    printpaths (abs_paths)
