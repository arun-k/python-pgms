import re
import urllib
import sys

def antihtml():
    if len(sys.argv) != 2:
        print "Format --\"URL\""
        exit()
    url=sys.argv[1]
    urlfile=urllib.urlopen(url)
    html=urlfile.read()
    unhtml=re.split('<.+?>',html,flags=re.DOTALL)
    for line in unhtml:
        print line

if __name__=='__main__':
    antihtml()
