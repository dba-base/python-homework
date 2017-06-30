__author__ = "xiaoyu hao"

#文件yesterday2中 binary 修改成world ，写入到也是terday.bak中
f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday2.bak","w",encoding="utf-8")

for line in f:
    if "binary" in line:
        line = line.replace("binary","world!")
    f_new.write(line)
f.close()
f_new.close()


