__author__ = "xiaoyu hao"

'''
选择数据源类型
'''

def file_db_handle(conn_params):
    '''
    解析文件
    :param conn_params: 字典
    :return: 文件的路径
    '''
    db_path = '%s/%s' %(conn_params['path'],conn_params['name'])
    return db_path

def mysql_db_handle():
    pass

def db_handler(conn_params):
    '''
    连接数据库
    :param conn_params: settings中数据库的参数信息
    :return: 要操作的方法
    '''

    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)

    if conn_params['engine'] == 'mysql':
        return mysql_db_handle()

