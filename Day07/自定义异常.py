

#自定义一个类
class AlexError(Exception):
    def __init__(self, msg):
        self.message = msg
    # def __str__(self):
    #     return 'sdfsf'
try:
    raise AlexError('数据库连不上')
except AlexError as e:
    print(e)