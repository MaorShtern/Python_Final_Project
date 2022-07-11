import pandas as pd
import pymssql
from SQL_Connection import Connect_to_SQL_Server,Connect_to_SQL_Server_Pymssql


def sort_by_category(e):
    return e['Category']


def create_list_of_categories(product_sales_table):
    category_list = []
    for temp_dict in product_sales_table:
        category_list.append(temp_dict['Category'])  # הכנסה לרשימה את הקטגוריות

    category_list = sorted(set(category_list))  # הורדת כפילויות של קטגוריות
    return category_list


def display_table_of_best_sellers(dictionary_of_best_sellers, category_list):
    """

    :param dictionary_of_best_sellers:   מילון של המוצרים הנמכרים ביותר מכל קטגוריה

    :param category_list: רשימת קטגוריות
    הפונקציה יוצרת מילון המורכב מקטגוריות מוצרים והכמות שלהם
    ושולחת את המילון שנוצר להדפסה
    """

    products = []
    amounts = []
    for dict_value in dictionary_of_best_sellers.values():
        amounts.append(dict_value[0])
        products.append(dict_value[1])

    data = {'Category': category_list, 'Product': products, 'Amount': amounts}
    print_df(data)


def most_products_sales_in_each_category():
    '''
    הפונצקיה מבצעת השמה של טבלת כל המכירות למשתנה , מבצעת השמה לרשימה רק את הקטגוריות הנמצאות בטבלה תיוצרת מילון שהמפתחות שלו הם הרשימה הנ"ל וערכיהם מאותחלים באפס
    המילון המעודכן לאחר ביצוע הלולאה נשלח להצגה

    '''
    product_sales_table = product_sales()
    category_list = create_list_of_categories(product_sales_table)

    dictionary_of_best_sellers = {key: [0] for key in
                                  category_list}
    for temp_dict in product_sales_table:  # עבור כל שורה בטבלת המכירות משווים כמות ומבצעים השמה של הכמות הגדולה ביותר מבין הערך הנ"ל או הערך שקיים במילון לכל קטגוריה בנפרד והשמה של שם המוצר במילון
        for category in category_list:
            if temp_dict['Category'] == category:
                if temp_dict['Amount'] > dictionary_of_best_sellers[category][0]:
                    dictionary_of_best_sellers[category][0] = temp_dict['Amount']
                    dictionary_of_best_sellers[category].append(temp_dict['Description'])
    display_table_of_best_sellers(dictionary_of_best_sellers, category_list)


def print_df(data):
    '''
    :param data: מידע במבנה של מילון
    הפונקציה יוצרת מסגרת תצוגה מהפרמטר שהתקבל ומדפיסה אותה
    '''
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


def get_product_sales():
    product_sales_table = product_sales()
    print_df(product_sales_table)


def product_sales():
    """
    הפונצקיה יוצרת חיבור עם מסד הנתונים ויוצרת רשימה של מילונים מערך המוחזר מפרוצדורה להצגת כל המכירות
    :return:result_rows :   רשימה של מילונים
    """
    cursor = Connect_to_SQL_Server_Pymssql()

    cursor.callproc('SumPerProduct')
    result_rows = [row for row in cursor]
    for row in cursor:
        result_rows.append(row)

    result_rows.sort(key=sort_by_category)

    return result_rows


def Product_Purchase_By_Code(product_code):
    product_list = []

    cursor = Connect_to_SQL_Server()
    for row in cursor.execute(f"exec ProductPurchaseByName '{product_code}'"):
        product_list.append(row)

    print(product_list)

