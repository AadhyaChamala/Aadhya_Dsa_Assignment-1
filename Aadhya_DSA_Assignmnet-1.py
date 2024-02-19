#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id, self.name, self.price, self.category = product_id, name, float(price), category

class ProductList:
    def __init__(self):
        self.products = []

    def insert(self, product_data):
        self.products.append(Product(*product_data))

    def display(self):
        for product in self.products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    def search_by_id(self, product_id):
        return next((product for product in self.products if product.product_id == product_id), None)

    def update(self, product_id, new_price):
        product = self.search_by_id(product_id)
        if product:
            product.price = float(new_price)
            print(f"Product with ID {product_id} updated successfully.")
        else:
            print(f"Product with ID {product_id} not found.")

    def delete(self, product_id):
        self.products = [product for product in self.products if product.product_id != product_id]
        print(f"Product with ID {product_id} deleted successfully.")

    def bubble_sort(self):
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]

def time_sorting_algorithm(sorting_func, product_list):
    start_time = time.time()
    sorting_func()
    end_time = time.time()
    return end_time - start_time

def main():
    product_list = ProductList()

    with open("product_data.txt", "r") as file:
        for line in file:
            product_data = line.strip().split(",")
            product_list.insert(product_data)

    print("Original Product List:")
    product_list.display()
    print("\n")

    product_list.insert(["12345", "Camera Covers", "15.99", "Electronics"])
    print("Product List after Insertion:")
    product_list.display()
    print("\n")

    product_list.update("87296", "290.00")
    print("Product List after Update:")
    product_list.display()
    print("\n")

    product_list.delete("44574")
    print("Product List after Deletion:")
    product_list.display()
    print("\n")
    
    

    # Sorting and measuring time on original data
    sorted_time = time_sorting_algorithm(product_list.bubble_sort, product_list)
    print(f"Bubble Sort Time on Original Data: {sorted_time:.6f} seconds")

    # Sorting and measuring time on reverse-sorted data
    reversed_list = ProductList()
    reversed_list.products = sorted(product_list.products, key=lambda x: x.price, reverse=True)
    reversed_sorted_time = time_sorting_algorithm(reversed_list.bubble_sort, reversed_list)
    print(f"Bubble Sort Time on Reverse-Sorted Data: {reversed_sorted_time:.6f} seconds")

    # Sorting and measuring time on already sorted data
    already_sorted_list = ProductList()
    already_sorted_list.products = sorted(product_list.products, key=lambda x: x.price)
    already_sorted_time = time_sorting_algorithm(already_sorted_list.bubble_sort, already_sorted_list)
    print(f"Bubble Sort Time on Already Sorted Data: {already_sorted_time:.6f} seconds")

if __name__ == "__main__":
    main()


# In[ ]:




