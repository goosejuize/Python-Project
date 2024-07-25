import datetime
import tkinter as tk
from tkinter import simpledialog
from appointment_handler import get_appointment, Appointment

# Custom exception for invalid input
class InvalidInputError(Exception):
    pass

# Product class to define art supplies
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ArtSupply(Product):
    def __init__(self, name, price, medium):
        super().__init__(name, price)
        self.medium = medium

# Order class to handle product selection
class Order:
    def __init__(self):
        self.items = {}  # Store items as a dictionary with quantities
        self.total_price = 0.0

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'price': product.price, 'medium': product.medium, 'quantity': quantity}
        self.total_price += product.price * quantity
        print(f"Added {product.name} (x{quantity}) to your order. Price: ${product.price:.2f} each")

    def get_receipt_summary(self):
        # Create a receipt summary string
        receipt_content = "Customer Receipt:\n"
        receipt_content += "Order Summary:\n"

        for product_name, details in self.items.items():
            receipt_content += f"Product: {product_name}, Price: ${details['price']:.2f}, Quantity: {details['quantity']}\n"
            receipt_content += f"Medium: {details['medium']}\n"

        receipt_content += f"Total Price: ${self.total_price:.2f}\n"
        return receipt_content

# Function to display available products
def display_products(products):
    print("Available Art Supplies:")
    for idx, product in enumerate(products, start=1):
        if isinstance(product, ArtSupply):
            print(f"{idx}. {product.name} - ${product.price:.2f} (Medium: {product.medium})")
        else:
            print(f"{idx}. {product.name} - ${product.price:.2f}")

# Function to get product selection from user
def get_product_selection(products):
    order = Order()
    while True:
        try:
            display_products(products)
            selection = input("Select a product by number (0 to finish): ")
            if not selection.isdigit():
                raise InvalidInputError("Invalid input. Please enter a number.")
            selection = int(selection)
            if selection == 0:
                break
            if selection < 1 or selection > len(products):
                raise InvalidInputError("Invalid product number. Please choose a number within the options.")

            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise InvalidInputError("Quantity must be greater than 0.")
                
            order.add_product(products[selection - 1], quantity)
        except InvalidInputError as e:
            print(e)
    return order

def store_receipt(receipt_content):
    """Function to store receipt information in a text file."""
    try:
        with open('customer_receipt.txt', 'w', encoding='utf-8') as file:
            file.write(receipt_content)
        print("Receipt stored in customer_receipt.txt")
    except Exception as e:
        print(f"Error saving receipt: {e}")

def read_receipt():
    """Function to read the receipt information from a text file."""
    try:
        with open('customer_receipt.txt', 'r', encoding='utf-8') as file:
            print(file.read())
    except Exception as e:
        print(f"Error reading receipt: {e}")

def main():
    # Define available art supplies
    products = [
        ArtSupply("Acrylic Paint Set", 25.99, "Acrylic"),
        ArtSupply("Watercolor Paint Set", 19.99, "Watercolor"),
        ArtSupply("Charcoal Pencils", 15.49, "Charcoal"),
        ArtSupply("Canvas Panels", 10.99, "Canvas"),
        ArtSupply("Paint Brushes", 12.50, "Synthetic"),
        ArtSupply("Graphite Pencils", 8.99, "Graphite"),
        ArtSupply("Pastels Set", 22.50, "Pastel"),
        ArtSupply("Easel Stand", 35.00, "Wood"),
    ]

    print("Welcome to Artiza!")
    order = get_product_selection(products)

    appointment = get_appointment()
    while appointment is None:
        appointment = get_appointment()

    # Get receipt summary
    receipt_content = order.get_receipt_summary()
    receipt_content += f"Appointment Date: {appointment.date}, Time: {appointment.time}\n"

    # Store the receipt
    store_receipt(receipt_content)

if __name__ == "__main__":
    main()

