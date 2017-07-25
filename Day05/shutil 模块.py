__author__ = "xiaoyu hao"

#高级的 文件、文件夹、压缩包 处理模块
import shutil

# 创建压缩包并返回文件路径，例如：zip、tar
#
#      base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
#      如：www                        =>保存至当前路径
#      如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
#      format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
#      root_dir：	要压缩的文件夹路径（默认当前目录）
#      owner：	用户，默认当前用户
#      group：	组，默认当前组
#      logger：	用于记录日志，通常是logging.Logger对象

#shutil.copy('笔记','笔记2')

# f1 = open("本节笔记",encoding="utf-8")
#
# f2 = open("笔记2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)r

#shutil.copyfile("笔记2","笔记3")
#shutil.copystat("本节笔记","笔记3")

#shutil.copytree("test4","new_test4")
#shutil.rmtree("new_test4")

#创建压缩包并返回文件路径，例如：zip、tar

shutil.make_archive("..\shutil_archive_test", "zip","F:\github\python_homework\Day05")

#shutil 对压缩包的处理是调用 ZipFile 和 TarFile 两个模块来进行的