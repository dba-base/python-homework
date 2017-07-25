__author__ = "xiaoyu hao"

import xml.etree.ElementTree as ET
tree = ET.parse('xmltest.xml')
root = tree.getroot()

for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    print(name, rank)

'''
输出：
Liechtenstein 2
Singapore 5
Panama 69
'''

#修改
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')  # 给rank添加属性


#删除
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('xmltest.xml')


