import tkcalendar as tkc
from tkcalendar import DateEntry
import tkinter as tk
import psycopg2


def insert_data():
    # Retrieves data from input fields
    name = name_entry.get()
    item_bought = item_entry.get()
    price = price_entry.get()
    date_of_purchase = date_entry.get_date()  # Get selected date 
    
    # Validation for the price field
    try:
        # Convert price to a float
        price = float(price)
        # Check if price is negative
        if price < 0:
            raise ValueError("Price cannot be negative.")
    except ValueError:
        # If conversion to float fails or price is negative
        status_label.config(text="Invalid price. Please enter a positive number.")
        return

    # AWS connection
    conn = psycopg2.connect(
        dbname='*******
        user='************
        password='***************
        host='*********************
        port='*******
    )
    
    cursor = conn.cursor()
    # SQL query
    sql = "INSERT INTO *********(name, item_bought, price, category, date_of_purchase) VALUES (%s, %s, %s, %s, %s)"
    # Execute query with the provided data
    cursor.execute(sql, (name, item_bought, price, category_value_inside.get(), date_of_purchase))
   
    conn.commit()
     cursor.close()
    conn.close()
     status_label.config(text="Data inserted successfully!")


root = tk.Tk()
root.title("Insert Data")

# Creates input fields and labels and places them on the app
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

item_label = tk.Label(root, text="Item Bought:")
item_label.grid(row=1, column=0, padx=10, pady=5)
item_entry = tk.Entry(root)
item_entry.grid(row=1, column=1, padx=10, pady=5)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=2, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=5)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=3, column=0, padx=10, pady=5)

# Category list
categories = ["Mortgage", "ADT bill", "Gas bill","Water Bill","Mattress Bill"," Groceries","Kitties","Trash Service",
              "Phone Bill","Wifi Bill","Water Filter Bill","Electric Bill","Solar Bill","Hulu","Netflix","Daycare"] 

# variable to hold the selected category
category_value_inside = tk.StringVar(root)
category_value_inside.set("Select an Option")

# Create the dropdown menu for categories
category_dropdown = tk.OptionMenu(root, category_value_inside, *categories)
category_dropdown.grid(row=3, column=1, padx=10, pady=5)

date_label = tk.Label(root, text="Date of Purchase:")
date_label.grid(row=4, column=0, padx=10, pady=5)
date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=4, column=1, padx=10, pady=5)

# Create button and place it on the app to insert data
insert_button = tk.Button(root, text="Insert Data", command=insert_data)
insert_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create label for status messages and place it on the app
status_label = tk.Label(root, text="")
status_label.grid(row=6, column=0, columnspan=2)


root.mainloop()





