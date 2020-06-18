"""
题目：将001中生成的激活码写入到MySQL中
题目解析：MySQL的使用
步骤：
    1.导入库文件
    2.连接数据库
    3.定义连接函数，创建MySQL表单
    4.读取激活码文档并写入数据库中
"""
# 导入库函数
import pymysql

# 连接数据库
con = pymysql.connect('localhost', 'root', 'niboxtt315426', 'mysql')

# 创建游标
cue = con.cursor()
print("connect success")

# 创建数据库表格
# 如果Keycode表存在则删除
cue.execute("DROP TABLE IF EXISTS Keycode")
sql = "CREATE TABLE Keycode(name varchar(255))"
cue.execute(sql)
print("create table success")


# 定义连接函数，创建MySQL表单
def install(con, name):

    # try-except捕获异常
    # 执行sql语句
    try:
        cue.execute("insert into Keycode(name) value(%s)", [name])
        print("insert success")
    except Exception as e:
        print("insert error", e)
        con.rollback()
    else:
        # 提交数据
        con.commit()


# 读取激活码文档并写入数据库中
def read_txt():
    with open('keycode.txt', 'r') as fp:
        datas = fp.readlines()
        print(datas[0])
    for data in datas:
        install(con, data)
        # print(data)
        # print(type(data))
    print("数据插入完成")


if __name__ == '__main__':
    read_txt()
    con.close()

