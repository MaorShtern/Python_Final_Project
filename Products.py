from SQL_Connection import Connect_to_SQL_Server
from matplotlib import pyplot as plt

cursor = Connect_to_SQL_Server()


def product_sales():
    result = []
    for row in cursor.execute("exec SumPerProduct"):
        result.append(row)

    for row in result:
        print(row)


if __name__ == '__main__':
    product_sales()