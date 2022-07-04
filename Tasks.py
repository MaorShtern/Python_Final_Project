from matplotlib import pyplot as plt
from SQL_Connection import Connect_to_SQL_Server


cursor = Connect_to_SQL_Server()


def Number_of_tasks_per_month():
    amount_of_room_service_requests = []
    dates = []

    for i in cursor.execute("SELECT Start_Date, count(Start_Date) FROM Employees_Tasks GROUP by Start_Date"):
        dates.append(i[0])
        amount_of_room_service_requests.append(i[1])

    print("amont of room service requests = ", sum(amount_of_room_service_requests))
    print("Dates = ", dates)

    plt.bar(dates, amount_of_room_service_requests)
    plt.ylim(0, max(amount_of_room_service_requests) + 1)
    plt.xlabel("Dates")
    plt.ylabel("Amount")
    plt.title("Amount of room service requests")
    plt.show()


if __name__ == '__main__':
    Number_of_tasks_per_month()
