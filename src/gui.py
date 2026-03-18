# importing modules

import tkinter as tk
from receipt import generate_receipt

def submit():
    name = name_entry.get()
    product = product_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    payment_method = payment_entry.get()

    file = generate_receipt(name, product, quantity, price, payment_method)
    status_label.config(text=f"✅ Saved: {file}")

root = tk.Tk()
root.title("Payment Receipt Generator")
root.geometry("350x350")

tk.Label(root, text="Customer Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Product").pack()
product_entry = tk.Entry(root)
product_entry.pack()

tk.Label(root, text="Quantity").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Label(root, text="Payment Method").pack()
payment_entry = tk.Entry(root)
payment_entry.pack()

tk.Button(root, text="Generate Receipt", command=submit).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()