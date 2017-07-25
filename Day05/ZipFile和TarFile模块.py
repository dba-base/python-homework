__author__ = "xiaoyu hao"


import zipfile
# 压缩
z = zipfile.ZipFile('test.zip', 'w')  #压缩包的名字
z.write('笔记')     #要压缩的文件名
z.write('随机数.py')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()


################################################################

import tarfile

# 压缩
tar = tarfile.open('your.tar','w')
tar.add('F:\github\python_homework\Day05\笔记', arcname='笔记')
tar.add('F:\github\python_homework\Day05\笔记2', arcname='笔记2')
tar.close()

# 解压
tar = tarfile.open('your.tar','r')
tar.extractall()  # 可设置解压地址
tar.close()


