import pymysql
from testspider import settings  # 引用 scrapy 框架配置文件


def readdata():
    # 连接数据库
    connectiontemp = pymysql.connect(
        host=settings.MYSQL_HOST,
        db=settings.MYSQL_DBNAME,
        user=settings.MYSQL_USER,
        passwd=settings.MYSQL_PASSWD,
        charset='utf8',
        use_unicode=True)
    cursortemp = connectiontemp.cursor()  # 通过 cursor 执行增删查改
    sql = "SELECT * FROM {0};".format(settings.MYSQL_TABLE)
    cursortemp.execute(sql)  # 执行 sql 语句，sql 语句参照 mysql 语法，字符串格式

    result = cursortemp.fetchall()  # 获取查询结果
    # print(result)
    connectiontemp.commit()  # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connectiontemp.close()  # 断开连接

    return result


readdata()
