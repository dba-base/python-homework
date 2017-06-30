#Author: xiaoyu hao

name = 'china\ttelecom'

print(name.capitalize())   #首字母大写
print(name.count("e"))     #统计e的个数
print(name.center(50,"-"))  #-------------------chinatelecom-------------------
print(name.endswith("com")) #True 判断是否以com结尾
print(name.expandtabs(tabsize=30)) #china                         telecom   把tab转换成30个空格

print(name.find("tele"))  #打印tele的开始位置
print('ab112'.isalnum())  #判断是否包含数字和字母
print('asdf'.isalpha())   #判断是否全是字母
print('1'.isdecimal())    #判断是否为十进制
print('1A'.isdigit())     #判断是否为数字
print(''.isidentifier())  #True 判断是不是一个合法的变量名
print('1A'.isspace())     #是否为空格
print('China'.istitle())  #首字母是否大写
print("CH".isupper())     #是否为大写


print(','.join(['1','2','3','4']))  #1,2,3,4

print(name.ljust(50,'*'))    #用*向左补齐50个字符
print(name.rjust(50,'*'))    #用*向右补齐50个字符
print('    chinatelecom    ')
print('    chinatelecom    '.strip())   #去掉两边的空格


p = str.maketrans('abcdefg','1234567')  #a=1,b=2,c=3 ....  替换值

print("ogg".translate(p))   #输出o77， 把 g --> 7

print('alex li'.replace('l','L'))  #aLex Li
print('alex li'.replace('l','L',1))  #aLex li 只替换一个

print('haoxy_and'.rfind('a'))  # 输出6 查到最右边a的位置

print('hao xy and ling lin '.split())  #['hao', 'xy', 'and', 'ling', 'lin']   字符串生成列表，以空格分割

print('1+2+3+4'.split('+'))  #['1', '2', '3', '4']

print('hao xy '.swapcase())  #HAO XY
print('hao xy '.title())    #Hao Xy


#format :
msg = "my name is {}, and age is {}"
print(msg.format("alex",22))

msg = "my name is {1}, and age is {0}"
print(msg.format("alex",22))

msg = "my name is {name}, and age is {age}"
print(msg.format(age=22,name="ale"))

#format_map
msg.format_map({'name':'alex','age':22})

