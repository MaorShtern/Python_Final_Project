from Customers_Rooms import Month_with_the_most_reservation
from Tasks import Number_of_tasks_per_month
import Products
from Financial import Rooms_Income, Purchase_Of_Goods_Expenses, Products_Income


def main():
    # Number_of_tasks_per_month()
    #Month_with_the_most_reservation()
    # Products.get_product_sales()
    # Products.most_products_sales_in_each_category()
    product_name = input("Product_Purchase_By_Code: ")
    Products.Product_Purchase_By_Code(product_code=product_name)
    goods_Expenses = Purchase_Of_Goods_Expenses()
    print(f"Purchase_Of_Goods_Expenses: {goods_Expenses}")
    rooms_Income_total = Rooms_Income()
    print(f"Rooms_Income: {rooms_Income_total}")
    products_Income = Products_Income()
    print(f"Products_Income: {products_Income}")
    print(f"General income: {rooms_Income_total + products_Income - goods_Expenses}")


if __name__ == '__main__':
    main()
