from Customers_Rooms import Month_with_the_most_reservation
from Tasks import Number_of_tasks_per_month
import Products


def main():
    #Number_of_tasks_per_month()
    #Month_with_the_most_reservation()
    # Products.get_product_sales()
    Products.most_products_sales_in_each_category()
    product_code = input("Product_Purchase_By_Code: ")
    Products.Product_Purchase_By_Code(product_code=product_code)


if __name__ == '__main__':
    main()
