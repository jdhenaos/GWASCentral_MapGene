
# coding: utf-8

# In[137]:

import urllib2
import sys

# In[155]:

infile = open(sys.argv[1])


# In[156]:

def MapGene(link):
    open_link = urllib2.urlopen(link)
    code_link = open_link.read()
    
    init_mark_link = code_link.find("<th>Marker accession ID</th>")
    white_spaces = code_link[init_mark_link+len("<th>Marker accession ID</th>"):code_link.find("</td>",init_mark_link+len("<th>Marker accession ID</th>"))]
    ID_SNP = white_spaces[9:-1]
    
    init_map_link = code_link.find("<th>Mapped gene</th>")
    white_spaces_map = code_link[init_map_link+len("<th>Mapped gene</th>"):code_link.find("</td>",init_map_link+len("<th>Marker accession ID</th>"))]
    map_gene = white_spaces_map[9:]
    
    open_link.close()
    print map_gene+"\t"+ID_SNP
    
for i in infile.readlines():
    pos_web_final = i.find("/",39)
    MapGene(i[0:pos_web_final])


# In[145]:

infile.close()


# In[ ]:



