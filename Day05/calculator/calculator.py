
'''
实现加减乘除及拓号优先级解析
用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
必须自己解析里面的(),+,-,*,/符号和公式
'''


# 小bug,无法计算类似 1 - 2 * ( (60-30 +(-4) )) 单独的-4 这种运算
# 缺少指数运算


import re
import os
import sys


def compute_Add_subtract(expression):
    '''
    加减运算
    :param expression:
    :return:
    '''
    #print("加减传入的值：",expression)
    pattern = re.compile(r'\d+\.?\d*[\+\-]{1}\d+\.?\d*')
    
    while True:
        if expression.__contains__('+-') \
                or expression.__contains__("++") \
                or expression.__contains__('-+') \
                or expression.__contains__("--"):
            expression = expression.replace('+-', '-')
            expression = expression.replace('++', '+')
            expression = expression.replace('-+', '-')
            expression = expression.replace('--', '+')
        else:
            break

    add_list = re.findall(r"-?\d+\.?\d*", expression)
    list = []
    for i in add_list:
        list.append(float(i))
    result = sum(list)
    return result

def compute_multiply_divide(expression):
    '''
    乘除运算
    :param expression:括号内的内容
    :return:做完加减乘除的表达式
    '''

    # 以 expression 等于 -40.0*5+23*2+2*6-3*6*2*2/2%2 为例

    #print("乘除传入的值：",expression)

    Flag = False

    pattern = re.compile(r'\d+\.?\d*[\*\/\%]+[\+\-]?\d+\.?\d*')

    while not Flag:
        match = pattern.search(expression)
        if match:

            match_content = match.group()

            if len(match_content.split('*')) > 1:
                n1, n2 = match_content.split('*')
                value = float(n1) * float(n2)
            elif len(match_content.split('//')) > 1:
                n1, n2 = match_content.split('//')
                value = float(n1) // float(n2)
            elif len(match_content.split('%')) > 1:
                n1, n2 = match_content.split('%')
                value = float(n1) % float(n2)
            elif len(match_content.split('/')) > 1:
                n1, n2 = match_content.split('/')
                value = float(n1) / float(n2)

            before, after = pattern.split(expression, 1)
            expression = '%s%s%s' % (before, value, after)  # 计算完乘除运算后的表达式
            #print(expression)
        else:
            Flag = True
    return expression




def compute_expon(expression):
    '''
    指数运算
    :param expression:
    :return:计算结果
    '''
    pass

def compute(expression):
    '''
    操作加减乘除指数
    :param expression:
    :return:计算结果
    '''
    #先乘除后加减
    #以-40.0/5+23*2 为例

    # 匹配乘除取余
    expression = compute_multiply_divide(expression)
    #print("乘除运算后返回值：",expression)
    
    #进行加减运算
    #匹配加减运算
    expression1 = compute_Add_subtract(expression)
    #print("加减运算后返回值",expression)
    return expression1


def deal_bracket(expression):
    '''
    递归处理括号
    :param expression:
    :return:
    '''
    #pattern = re.compile(r'\(([\+\-\*\/]*\d+\.*\d*){2}\)')    #匹配括号中的内容
    pattern = re.compile(r'\(([\+\-\*\/\%\/\/\*\*]*\d+\.*\d*){2,}\)')

    #判断是否还有括号，没有的话计算最后的结果并返回
    if not pattern.search(expression):
        final_result = compute(expression)
        return final_result

    #获取第一个最内层括号内容
    content = pattern.search(expression).group()
    #print("第一层括号：",content)
    #分割表达式，把表达式分成三部分，通过使用re模块的split函数，使用正则表达式对字符串进行分割，1为分割一次
    before,middle,end = pattern.split(expression,1)

    print("Before",expression)
    content=content[1:len(content)-1]
    #print("括号中的内容:",content)
    #计算括号内的内容，并取得结果
    result = compute(content)

    print('%s = %s'% (content,result))  #输出括号的结果

    #拼接新的表达式
    expression = '%s%s%s' %(before,result,end)
    print('after:',expression)
    print("="*10,"上一次计算","="*10)

    return deal_bracket(expression)

def main():

    flag = True

    os.system('clear')   # 清屏


    print('\n================================================================')
    print('\033[33m 欢迎使用计算器\033[0m')
    print('\n================================================================')

    while flag:
        calculator_input = input('\033[32m请输入计算的表达式 | (退出:q)\033[0m')

        #expression = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

        expression = calculator_input.replace(' ','')  #去除所有的空格

        if len(expression) == 0:
            continue
        elif calculator_input == 'q':
            sys.exit('\033[32m感谢使用\033[0m')
        elif re.search('[^0-9\.\-\+\*\/\%\/\/\*\*\(\)]',expression):
            print('\033[32m输入错误！\033[0m')
        else:
            final_result = deal_bracket(expression)
            print('the expression result is %s' % final_result)

if __name__ == '__main__':
    main()
