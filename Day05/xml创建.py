__author__ = "xiaoyu hao"

import xml.etree.ElementTree as ET

new_xml = ET.Element("personinfolist")

personinfo = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "yes"})
name = ET.SubElement(personinfo, "name")
name.text = 'xiaoyu'
age = ET.SubElement(personinfo, "age", attrib={"checked": "no"})
sex = ET.SubElement(personinfo, "sex")
age.text = '22'
sex.text = 'man'

personinfo2 = ET.SubElement(new_xml, "personinfo", attrib={"enrolled": "no"})
name2 = ET.SubElement(personinfo2, "name")
age = ET.SubElement(personinfo2, "age")
sex = ET.SubElement(personinfo2, "sex")
name2.text = 'anglela'
age.text = '19'
sex.text = 'female'

et = ET.ElementTree(new_xml)  # 生成文档对象
et.write("test.xml", encoding="utf-8", xml_declaration=True)

ET.dump(new_xml)  # 打印生成的格式