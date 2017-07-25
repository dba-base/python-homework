__author__ = "xiaoyu hao"

import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()

print(root.tag)
print(root[0][1].text)

#遍历
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib)

#
for node in root.iter('year'):
    print(node.tag,node.text)

#Finding interesting elements
print('neighbor:')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

#
for country in root.findall('country'):   #root下的country标签
    name = country.get('name')            #
    rank = country.find('rank').text      # country 下的rank标签
    print(name, rank)

'''
输出：
Liechtenstein 2
Singapore 5
Panama 69
'''

