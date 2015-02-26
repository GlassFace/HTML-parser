from bs4 import BeautifulSoup
import sys
import codecs
import re

if sys.stdout.encoding != 'cp850':
    sys.stdout = codecs.getwriter('cp850')(sys.stdout, 'strict')
if sys.stderr.encoding != 'cp850':
    sys.stderr = codecs.getwriter('cp850')(sys.stderr, 'strict')
for num in range(1, 5269):
    soup = BeautifulSoup(open("html data/hu43_%i.html" % (num)))

    for link in soup.find_all('link'):
        var_link = link.get('href')
        if(var_link[0:4] =='show'):
            url = var_link

            append_string = "http://www.anime-forums.com/"
            url = "".join((append_string, url))
            ' '.join(url.split())
            url=re.sub(r"\s+", " ", url)
 
#for title searching
    for title in soup.find_all('title'):
        var_title = title.get_text()
        ' '.join(var_title.split())
        var_title=re.sub(r"\s+", " ", var_title)
        

#for body searching


        var_body=[]
        for body in soup.find_all('blockquote'):
            var_body.append(body.get_text())

    try:
        file=open("txt data/hu43_%i.txt"% (num), 'a')
        file.write(url+'\n')
        file.write(var_title+'\n')
        for z in var_body:
            #z = unicode(z, "utf-8", errors="ignore")
            ' '.join(z.split())
            z=re.sub(r"\s+", " ", z)
            file.write(z+'\n')
    except IOError:
        print "Error: can\'t find file or read data"
    else:
        print "Written content in the file successfully"
        print "done processing hu43_%i.html" % (num)
        file.close()
