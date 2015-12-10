from __future__ import division
import sys; import os;
template_name = 'design'; base_html = sys.argv[1]; output = sys.argv[2];

def get_template(fname):
    f = open(fname, 'r')
    template =  f.readlines()
    l = len(template)
    return template, l

def get_basehtml(fname):
    f2 = open(fname,'r')
    raw_html = f2.readlines()
    return raw_html

temp, li = get_template(template_name)
raw = get_template(base_html)

f3 = open(output,'w')

for i in range(li-7):
    f3.writelines(temp[i])
for i in range(len(raw[0])):
    f3.writelines(raw[0][i])
for i in range(li-7, li, 1):
    f3.writelines(temp[i])
    
f3.close()
