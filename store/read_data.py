from products.models import Products
from customers.models import Customers, Address, CustomerSegment
from sales.models import Sales
from orders.models import Orders
from shipments.models import Shipments
import csv


with open('Central_Superstore.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=",")
    for i,line in enumerate(lines):
        if  i == 0:
            continue
        orderId = line[1]
        orderDate = line[2]
        shipDate = line[3]
        shipMode = line[4]
        customerId = line[5]
        customerName = line[6]
        segment = line[7]
        country = line[8]
        city = line[9]
        state = line[10]
        zipcode = line[11]
        region = line[12]
        productId = line[13]
        category = line[14]
        subCategory = line[15]
        productName = line[16]
        salesIncome = line[17]
        quantity = line[18]
        discount = line[19]
        profit = line[20]

        print customerName

