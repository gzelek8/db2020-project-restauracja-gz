import tkinter as tk
from tkinter import messagebox

from src.sql import sql_query


def show_orders(login_window):
    """Funckja wyświetlająca aktualne zamówienia znajdujące się w bazie dnaych
        @Argumenty:
                    login_window(tk.TK)"""

    def log_out():
        """Funkcja służąca do wylogowania aktualnego użytkownika"""
        logout_var = messagebox.askyesno("Logout", "Logout?")
        if logout_var > 0:
            login_window.update()
            login_window.deiconify()
            order_menu.destroy()

    def find_order_id(order):
        """Funkcja znajdująca id danego zamówienia
            @argumenty: order(string)
            @return order_id(int)"""
        string_split = order.split()
        string_split_next_lvl = string_split[1].split('.')
        order_id = string_split_next_lvl[1]
        return int(order_id)

    def update_status_of_orders():
        """Funkcja zmieniająca status zamówienia na gotowe oraz wywołująca metode usuwające je z bazy danych"""
        index_of_orders = list_of_orders_listbox.curselection()
        order_string = list_of_orders_listbox.get(index_of_orders)
        order_id = find_order_id(order_string)
        list_of_orders_listbox.delete(index_of_orders)
        sql_query.delete_orders_from_database(order_id)
        tk.messagebox.showinfo("Meal ready", "Meal ready")

    # Window configuration
    order_menu = tk.Toplevel()
    order_menu.title("AGZ Restaurant")
    order_menu.iconbitmap(r'..\..\resources\graphics\lg.ico')

    # Get data from database and prepare
    list_of_orders = sql_query.get_all_order()
    list_of_orders_index = []
    for order in list_of_orders:
        list_of_orders_index.append(order[0])
    list_of_orders_index = list(dict.fromkeys(list_of_orders_index))
    finally_list_of_orders = []
    for counter, index in enumerate(list_of_orders_index):
        temporary_list_of_orders = []
        temporary_list_of_orders.append(f"Order nr.{index}")
        for order in list_of_orders:
            if order[0] == index:
                temporary_list_of_orders.append(f" {order[1]} - ({order[2]}) ")
        finally_list_of_orders.append(temporary_list_of_orders)
    # List of actual orders
    list_of_orders_listbox = tk.Listbox(order_menu, selectmode='single', width=200)
    tk.Button(order_menu, text="Ready", command=update_status_of_orders).grid(row=1, columnspan=2)
    for counter, order in enumerate(finally_list_of_orders):
        list_of_orders_listbox.insert(counter, ''.join(map(str, order)))
    list_of_orders_listbox.grid(row=0, column=0)
    log_out_button = tk.Button(order_menu, text="Log out", command=log_out)
    log_out_button.grid(row=2, column=0)

    order_menu.mainloop()
