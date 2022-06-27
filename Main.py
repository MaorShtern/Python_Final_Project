import pyodbc
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

server = 'sql5108.site4now.net'
database = 'db_a79b5b_proj13'
username = 'db_a79b5b_proj13_admin'
password = 'XXNEA6q6VbvATG6g'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


def greph_data():
    # for i in cursor.execute("select Task_Number, Start_Date from Employees_Tasks"):
    amont_of_room_service_requests = []
    dates = []

    for i in cursor.execute("SELECT Start_Date, count(Start_Date) FROM Employees_Tasks GROUP by Start_Date"):
        dates.append(i[0])
        amont_of_room_service_requests.append(i[1])

    print("amont of room service requests = ", amont_of_room_service_requests)
    print("Dates = ", dates)

    # plt.bar to plot a bar graph
    # with given values
    plt.bar(dates, amont_of_room_service_requests)

    # Setting count of values in
    # y-axis
    plt.ylim(0,5)

    # setting xlabel of graph
    plt.xlabel("Dates")

    # setting ylabel of graph
    plt.ylabel("Amount")

    # setting tile of graph
    plt.title("Amount of room service requests")

    # show() method to display the graph
    plt.show()


# Connecting to SQL and returning the Cursor so we can work on the database
# def Connect_to_SQL_Server():
#     server = 'sql5108.site4now.net'
#     database = 'db_a79b5b_proj13'
#     username = 'db_a79b5b_proj13_admin'
#     password = 'XXNEA6q6VbvATG6g'
#     cnxn = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = cnxn.cursor()
#     return cursor


def main():
    # cursor = Connect_to_SQL_Server()
    # cursor.execute('exec GetAllEmployees')
    # for i in cursor:
    #     print(i)
    greph_data()


if __name__ == '__main__':
    main()
