import pyodbc


# Connecting to SQL and returning the Cursor so we can work on the database
def Connect_to_SQL_Server():
    server = 'sql5108.site4now.net'
    database = 'db_a79b5b_proj13'
    username = 'db_a79b5b_proj13_admin'
    password = 'XXNEA6q6VbvATG6g'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    return cursor


def main():
    cursor = Connect_to_SQL_Server()
    cursor.execute('exec GetAllEmployees')
    for i in cursor:
        print(i)


if __name__ == '__main__':
    main()