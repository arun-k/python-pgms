import sys
import os
import time

def list_filesinfo():
    if len(sys.argv) != 2:
        print "Format --\"dir-name\""
        exit()
    try:
        dir_name=sys.argv[1]
        files = os.listdir(dir_name)
        for f in files:
            if not os.path.isdir(os.path.join(dir_name,f)):
                stat=os.stat(f)
                print f + "\t" + str(stat.st_size) + "\t" + time.asctime(time.localtime(stat.st_mtime))
    except OSError,e:
        print "An error occured\n%s"%str(e)

if __name__=='__main__':
    list_filesinfo()
