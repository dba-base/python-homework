#Author: xiaoyu hao

product_list = [('iphone 5',3000),
                ('iphone 5s', 4000),
                ('iphone 6', 5000),
                ('iphone 6s', 6000),
                ('iphone 7', 7000),
                ('watch', 300),
                ('bike', 800)]

shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            #print(product_list.index(item),item)
            print(index,item)
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，啥也买不起了，去挣钱再来吧！\033[0m"%salary)
            else:
                print("prodeuct code [%s] is not exist!"%user_choice)
        elif user_choice == 'q':
            print("----------shopping list -----------------")
            for i in shopping_list:
                print(i)
            print("You current balance:%s" %salary)
            exit()
        else:
            print('invalid option...')
else:
    print("invalid option...")