__author__ = "xiaoyu hao"

import random

checknum = ''
random_count = 6

for i in range(random_count):
    current = random.randint(0,random_count)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checknum += str(tmp)

print(checknum)