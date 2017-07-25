__author__ = "xiaoyu hao"

import yaml

# {'plain': 'Scroll of Remove Curse',
# 'literal':
#     'by hjw              ___\n'
#     '   __              /.-.\\\n'
#     '  /  )_____________\\\\  Y\n'
#     ' /_ /=== == === === =\\ _\\_\n'
#     '( /)=== == === === == Y   \\\n'
#     ' `-------------------(  o  )\n'
#     '                      \\___/\n',
# 'single-quoted': 'EASY_KNOW',
# 'double-quoted': '?',
# 'folded': 'It removes all ordinary curses from all equipped items. Heavy or permanent curses are unaffected.\n'}


# document = """
#   a: 1
#   b:
#     c: 3
#     d: 4
# """
# print(yaml.dump(yaml.load(document)))

#读取yaml文件
f = open('test.yaml')
x = yaml.load(f)
print(type(x))
print(x)

'''
读取出来的内容是一个字典
<class 'dict'>
{'name': 'Tom Smith', 'age': 37, 'spouse': {'name': 'Jane Smith', 'age': 25}, 'children': [{'name': 'Jimmy Smith', 'age': 15}, {'name1': 'Jenny Smith', 'age1': 12}]}
'''

w = \
    {'name': 'Tom Smith',
     'age': 37,
     'spouse':
         {'name': 'Jane Smith',
          'age': 25},
     'children': [{'name': 'Jimmy Smith',
                   'age': 15},
                  {'name1': 'Jenny Smith',
                   'age1': 12}]}

f = open('newtree.yaml','w')
yaml.dump(w,f)
f.close()

'''
输出的格式稍微不一样
age: 37
children:
- {age: 15, name: Jimmy Smith}
- {age1: 12, name1: Jenny Smith}
name: Tom Smith
spouse: {age: 25, name: Jane Smith}
'''