__author__ = "xiaoyu hao"

# os.walk()的使用
import os


# 枚举dirPath目录下的所有文件,root 根目录，dirs 更目录下的目录，files根目录下的文件

def main():
    # begin
    fileDir = "F:" + os.sep + "mysql"  # 查找F:\aaa 目录下
    for root, dirs, files in os.walk(fileDir):
        # begin
        print("root:",root)
        print("dirs:",dirs)
        print("files",files)
        print(os.path.splitext("F:\github\python_homework\Day05\ATM\db\accounts\haoxy.json"))
        # end
    #os.system("pause")


# end

if __name__ == '__main__':
    # begin
    main()
    # end