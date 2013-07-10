import re
import sys
import urllib

def link():
    if len(sys.argv) != 2:
        print 'Format --"URL"'
        exit()
    try:
        URL=sys.argv[1]
        urlfile=urllib.urlopen(URL)
        body=urlfile.read()
        urls=re.findall(r'<a.*?href=\"(.+?)\".*?>',body)
        if urls:
            for url in urls:
                print url
        else:
            print "No URLs in this page"
    except re.error:
        print "Invalid string"

if __name__=='__main__':
    link()
