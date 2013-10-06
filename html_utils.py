BAD_TAGS = 'div,center,table,tbody,tr,td,img'.split(',')

from lxml import etree
import os
def strip_tags_lxml(html, tags):
  tree = etree.HTML(html)
  for tag in tags:
    etree.strip_tags(tree, tag)
  t = etree.tostring(tree, pretty_print=True)
  return os.linesep.join([s for s in t.splitlines() if s.strip()])
  
    
def clean_html(html):
  return strip_tags_lxml(html, BAD_TAGS)