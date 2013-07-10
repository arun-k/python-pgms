import json
import urllib

def myip():
        urlfile=urllib.urlopen('http://httpbin.org/get')
        body=urlfile.read()
        dic=json.loads(body)
        print dic["origin"]

if __name__=='__main__':
    myip()
