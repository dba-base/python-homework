#Author: xiaoyu hao

#浅copy的作用,共同账号
import  copy

person = ["name",["saving",1000]]

'''
浅copy的3几种方式：
p1=person[:]
p2=list(person)
p3=copy.copy(person)
'''

p1=person[:]
p2=person[:]

p1[0] = 'haoxy'
p2[0] = 'bingbing'

print(p1)
print(p2)

p1[1][1] = 50

print(p1)
print(p2)
