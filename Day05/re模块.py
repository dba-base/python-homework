import re

print(re.search('(abc){2}',"abcacabcasdf") )

print(re.search('\A[0-9]+[a-z]+\Z','1234asd'))  #1234asd
print(re.search('\A\w+\Z','1234asd'))  #同上

print(re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","asdfg12345asdf@13").groupdict())  #{'id': '12345', 'name': 'asdf'}

print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city"))

'''
输出：
{'province': '3714', 'city': '81', 'birthday': '1993'}
'''

print(re.split("[0-9]+","abc123f23GH"))  #['abc', 'f', 'GH']   按数字分隔

#替换
print(re.sub("[0-9]+","...","abc123f23GH23aa23bb"))  #abc...f...GH...aa...bb
print(re.sub("[0-9]+","...","abc123f23GH23aa23bb",2))  # 只替换前两个abc...f...GH23aa23bb

#re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
res = re.search("[a-z]+","asdASD",flags=re.IGNORECASE) #asdASD
print(res)

str = '''
abcd
\nbdsd
\nasdf
'''
res1 = re.search("[a-z]+d$",str,flags=re.MULTILINE)
print(res1)