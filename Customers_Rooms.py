from SQL_Connection import Connect_to_SQL_Server
from matplotlib import pyplot as plt

cursor = Connect_to_SQL_Server()


def Month_with_the_most_reservation():
    result = []
    for row in cursor.execute("exec Month_with_the_most_reservation"):
        result.append(row[0])

    result = list(set(list(map(lambda x: (x, result.count(x)), result))))

    months = list(map(lambda number_of_month: number_of_month[0], result))
    amount = list(map(lambda amount_of_month: amount_of_month[1], result))

    for item in result:
        months.append(item[0])
        amount.append(item[1])

    plt.bar(months, amount)
    plt.ylim(0, max(amount) + 1)
    plt.xlabel("MONTH")
    plt.ylabel("Amount")
    plt.title("Month with the most reservation")
    plt.show()


if __name__ == '__main__':
    Month_with_the_most_reservation()
