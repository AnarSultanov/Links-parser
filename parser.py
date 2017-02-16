import urllib.request, urllib.error, urllib.parse, sys
from html.parser import HTMLParser

links = []

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        for name, value in attrs:
            if name == "href":
                links.append(value)
                print (value)
 
def extract():
    if len(sys.argv) != 2:
        print('Usage: parser.py <URL for parsing>'.format(sys.argv[0]))
        return
    url = sys.argv[1]
 
    try:
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        f = urllib.request.urlopen(req)
        html = f.read()
        f.close()
    except urllib.error.HTTPError as e:
        print(e, 'while fetching', url)
        return


    parser = MyHTMLParser()
    parser.links = []
    parser.feed(html.decode('utf-8'))
    for l in links:
        print (l)
        
extract()