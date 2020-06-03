import tkinter as tk

from src.sql import sql_query


def show_orders():
    """Funckja wyświetlająca aktualne zamówienia znajdujące się w bazie dnaych"""
    # Window configuration
    order_menu = tk.Toplevel()
    order_menu.title("AGZ Restaurant")
    order_menu.iconbitmap(r'..\..\resources\graphics\lg.ico')

    # List of users -  pole tekstowe wyświetlające aktualnych użytkowników

    list_of_orders_text = tk.Text(order_menu)
    list_of_orders = sql_query.get_all_order()
    list_of_orders_index = []
    for order in list_of_orders:
        list_of_orders_index.append(order[0])
    list_of_orders_index = list(dict.fromkeys(list_of_orders_index))
    for index in list_of_orders_index:
        list_of_orders_text.insert(tk.END, f"Order nr.{index} ")
        for order in list_of_orders:
            if order[0] == index:
                list_of_orders_text.insert(tk.END, f"{order[1]} - {order[2]}; ")
        list_of_orders_text.insert(tk.END, '\n')

    list_of_orders_text.grid(row=0, column=0)
    list_of_orders_text.configure(state='disabled')

    order_menu.mainloop()

