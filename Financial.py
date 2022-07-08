from SQL_Connection import Connect_to_SQL_Server

cursor = Connect_to_SQL_Server()


def Rooms_Income():
    sum_total = 0
    for row in cursor.execute("Calu_Rooms_Income"):
        sum_total += row[0]
    print(f"Rooms_Income: {sum_total}")


def Purchase_Of_Goods_Expenses():
    sum_total = 0
    for row in cursor.execute("Expenses"):
        sum_total += row[0]
    print(f"Purchase_Of_Goods_Expenses: {sum_total}")


def Products_Income():
    sum_total = 0
    for row in cursor.execute("Calu_Products_Income"):
        if row[2] == 0:
            sum_total += row[0] * row[1]
        else:
            sum_total += ((row[1] * row[2]) / 100) * row[0]
    print(f"Products_Income: {sum_total}")