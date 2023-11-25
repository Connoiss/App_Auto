import pymysql


def check_data_existence(column,value):
    try:
        # 连接到 MySQL 数据库
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='remaimai'
        )

        # 创建游标对象
        cursor = connection.cursor()

        # 执行查询，检查数据是否存在
        query = f"SELECT * FROM re2 WHERE {column} = %s"
        cursor.execute(query, (value,))

        # 获取查询结果
        result = cursor.fetchone()

        # 检查结果是否存在
        if result:
            print(result[4])
        else:
            print(0)

    except pymysql.Error as err:
        print(f"Error: {err}")

    finally:
        # 关闭连接
        if connection and connection.open:
            cursor.close()
            connection.close()



# 使用示例
check_data_existence(
    column='user_name',
    value='123456'
)
