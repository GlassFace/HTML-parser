import sys
import codecs
import re


for num in range(1, 5269):
    file = open("txt data/hu43_%i.txt" % (num), 'r')
#file = open("txt data/hu43_3.txt", 'r')
    id = 'hu43_%i.txt' %(num)
#id = 'hu43_1.txt'
    id.replace("\n", "\\n")
    try:
        bulk_file=open("bulk.txt", 'a')
    except IOError:
        print "Error: can\'t find file or read data"
    
    lines = file.readlines()
    url = lines[0]
    url=re.sub(r"\s+", " ", url)
    url.replace("\n", "\\n")
    title = lines[1]
    title.replace("\n", "\\n")
    title=re.sub(r"\s+", " ", title)
    if(len(lines)>2):
        final_line = lines[2]
        final_line.replace("\n", "\\n")
        final_line=re.sub(r"\s+", " ", final_line)
    else:
        final_line = ''
    if(len(lines)>3):
        for i in range(3, len(lines)):
            line = lines[i]
            line.replace("\n", "\\n")
            line=re.sub(r"\s+", " ", line)
            final_line = final_line + line
  
    bulk_file.write('{ "create": { "_index": "hu43_index", "_type": "doc"}}"')
    bulk_file.write('\n')
    bulk_file.write(  '{"doc_id": "%s",  "url" : "%s", "title" : "%s", "body" : "%s"}' %(id,url.strip(),title.strip(),final_line.strip() ))
    bulk_file.write('\n')
    file.close()
    bulk_file.close()
    print "Written content in the file successfully"
    print "done processing hu43_%i.html" % (num)