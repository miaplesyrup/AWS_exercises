# pylint: disable=missing-module-docstring
# import csv
# import copy

# # IMPORT TABLE
# header = []
# table=[]
# pattern={}

# # GET HEADER
# with open('hardwareStore.csv') as file:
#     reader = csv.reader(file, delimiter=',')   
#     for row in list(reader)[0]:
#         header.append(row)

# # CREATE PATTERN
# for column in header:
#     pattern[column]=""

# # GET ELEMENTS FROM PATTERN AND CREATE TABLE
# with open('hardwareStore.csv') as file:
#     reader = csv.reader(file, delimiter=',')
    
#     for row in list(reader)[1:]:
#         element = copy.deepcopy(pattern)
#         x = 0
#         while x < len (header):
#             element[header[x]]=row[x]
#             x += 1
#         table.append(element)

# # PRINT TABLE WITH CUTE BORDER EME HAHA :) Pwede irun if gusto with borders haha
# # print("{}\n|{}{}|{}|\n{}".format(
# #     "".center(62,'-'),
# #     "".rjust(3, ' '),
# #     "PRODUCT_NAME".ljust(40,' '),
# #     "QUANTITY".center(16,' '),
# #     "".center(62,'-')
# # ))
# # table.sort(key=lambda x: int(x.get('QUANTITY')), reverse=True)
# # for item in table[:10]:
# #     print ("|{}{}|{}|\n{}".format(
# #         "".rjust(3,' '),
# #         item["PRODUCT_NAME"].ljust(40,' '),
# #         item["QUANTITY"].center(16,' '),
# #         "".center(62,'-')
# #     ))

# # PRINT TOP 10 HIGHEST QUANTITY PRODUCTS
# print("\nTOP 10 HIGHEST QUANTITY PRODUCTS\n{}{}".format(
#     "PRODUCT_NAME".ljust(40,' '), #ljust and center print format ng strings. (x, 'y') x = number of spacers; y = type of spacer
#     "QUANTITY".center(16,' ')
# ))
# table.sort(key=lambda x: int(x.get('QUANTITY')), reverse=True) #important to to convert to int() in x.get overwise it will be sorted/treated as a string
# for item in table[:10]:
#     print ("{}{}".format(
#         item["PRODUCT_NAME"].ljust(40,' '),
#         item["QUANTITY"].center(16,' ')
#     ))

# # GET SUM OF ITEMS PER CATEGORY
# category_sum = {}
# for item in table:
#     if item['CATEGORY_NAME'] in category_sum:
#         category_sum[item['CATEGORY_NAME']] += 1
#     else:
#         category_sum[item['CATEGORY_NAME']] = 1

# print('\nNUMBER OF ITEMS PER CATEGORY\n{}{}'.format(
#     'CATEGORY'.ljust(40,' '),
#     'NUMBER OF PRODUCTS'.center(16,' ')
# ))
# for key, value in category_sum.items():
#     print('{}{}'.format(
#         key.ljust(40, ' '),
#         str(value).center(16, ' ')
#     ))




# import csv
# from collections import defaultdict

# # Load data from the CSV file into a list of dictionaries
# file_path = 'hardwarestore.csv'
# data = []
# with open(file_path, 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)

# # Create a dictionary to store the total quantity per product
# product_counts = defaultdict(int)

# # Iterate through the data and calculate the total quantity per product
# for item in data:
#     product = item['PRODUCT_NAME']
#     quantity = int(item['QUANTITY'])
    
#     # Accumulate quantities for each product
#     product_counts[product] += quantity

# # Sort the products by quantity in descending order
# sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)

# # Print the top 10 products and their quantities
# print("Top 10 Products with Quantity:")
# for product, quantity in sorted_products[:10]:
#     print(f"{product}: {quantity}")



# import csv
# from collections import defaultdict

# # Load data from the CSV file into a list of dictionaries
# file_path = 'hardwarestore.csv'
# data = []
# with open(file_path, 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)

# # Create a dictionary to store the total quantity per product
# product_counts = defaultdict(int)

# # Iterate through the data and calculate the total quantity per product
# for item in data:
#     product = item['PRODUCT_NAME']
#     quantity = int(item['QUANTITY'])
    
#     # Accumulate quantities for each product
#     product_counts[product] += quantity

# # Sort the products by quantity in descending order
# sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# # Print the table with headers
# print("{:<20} {:<10}".format("PRODUCT_NAME", "QUANTITY"))
# print("-" * 30)
# for product, quantity in sorted_products:
#     print("{:<20} {:<10}".format(product, quantity))


# import csv
# from collections import defaultdict
# from tabulate import tabulate

# # Load data from the CSV file into a list of dictionaries
# file_path = 'hardwarestore.csv'
# data = []
# with open(file_path, 'r', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)

# # Create a dictionary to store the total quantity per product
# product_counts = defaultdict(int)

# # Iterate through the data and calculate the total quantity per product
# for item in data:
#     product = item['PRODUCT_NAME']
#     quantity = int(item['QUANTITY'])
    
#     # Accumulate quantities for each product
#     product_counts[product] += quantity

# # Sort the products by quantity in descending order
# sorted_products = sorted(product_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# # Convert the sorted products into a list of lists for tabulate
# table_data = [['PRODUCT_NAME', 'QUANTITY']]
# table_data.extend(sorted_products)

# # Print the table with headers
# table = tabulate(table_data, headers='firstrow', tablefmt='fancy_grid')
# print(table)

import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('hardwarestore.csv')

# Group the data by category and sum the quantities within each category
category_counts = df.groupby('PRODUCT_NAME')['QUANTITY'].sum()

# Sort the categories by quantity in descending order and select the top 10
top_10_categories = category_counts.sort_values(ascending=False).head(10)

# Print the top 10 categories and their quantities
print("Top 10 Categories with Quantity:")
print(top_10_categories)

# Iterate through the top 10 categories and print the items in each category with their quantities
for category in top_10_categories.index:
    items_in_category = df[df['PRODUCT_NAME'] == category]
    top_10_items = items_in_category.nlargest(10, 'QUANTITY')
    print(f"\nTop 10 items in {category}:")
    print(top_10_items[['PRODUCT_NAME', 'QUANTITY']])
