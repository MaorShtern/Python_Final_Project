import pandas as pd
import pymssql


def product_sales():
    conn = pymssql.connect(server='sql5108.site4now.net',
                           user='db_a79b5b_proj13_admin', password='XXNEA6q6VbvATG6g', database='db_a79b5b_proj13')
    cursor = conn.cursor(as_dict=True)

    cursor.callproc('SumPerProduct')
    rows = [row for row in cursor]
    for row in cursor:
        rows.append(row)

    df = pd.DataFrame(rows)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


if __name__ == '__main__':
    product_sales()
