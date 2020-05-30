"""
Moduł który zawiera funkcje służace do nawigacji w aplikacji , oraz tworzący podstawowe okno(menu)
 oraz system logownia użytkownika
"""

import tkinter as tk
from tkinter import messagebox

from src.app import admin_panel, order, reservation
from src.sql import sql_query


def show_order_window(menu_window):
    """Funkcja która uruchamia moduł order.
     Argument:
        @menu_window(tk.Toplevel)"""
    menu_window.withdraw()
    order.show_menu_window()
    menu_window.update()
    menu_window.deiconify()


def log_out(menu_window):
    """Funkcja służąca do wylogowania aktualnego użytkownika
    Argument:
        @menu_window(tk.Toplevel)"""
    logout_var = messagebox.askyesno("Logout", "Logout?")
    if logout_var > 0:
        login_window.update()
        login_window.deiconify()
        menu_window.destroy()


def exit_program():
    """Funkcja zamykająca cały program"""
    exit_var = messagebox.askyesno("Quit order", "Do you want to quit?")
    if exit_var > 0:
        login_window.destroy()
        login_window.quit()


def show_menu(login):
    """Funckja wyświetlająca opcje menu użytkownika po pomyslnym zalogowaniu
    Argument:
        @login(string)"""
    menu_window = tk.Toplevel()
    menu_window.title("AGZ Restaurant")
    menu_window.iconbitmap(r'..\..\resources\graphics\lg.ico')

    # Actual Workers
    personality_actual_employee = sql_query.get_name_actual_employee(login)
    actual_employee = tk.Label(menu_window, text="Now working: " + personality_actual_employee)
    actual_employee.grid(row=0, column=0)

    # Buttons
    orders_button = tk.Button(menu_window, text='Orders', padx=100, pady=10,
                              command=lambda: show_order_window(menu_window))
    orders_button.grid(row=1, column=0, sticky="ew")

    reservations_button = tk.Button(menu_window, text='Reservations', padx=100, pady=10,
                                    command=lambda: reservation.calendar(login))
    reservations_button.grid(row=2, column=0, sticky="ew")

    log_out_button = tk.Button(menu_window, text='Log out', padx=100, pady=10, command=lambda: log_out(menu_window))
    log_out_button.grid(row=3, column=0, sticky="ew")

    exit_button = tk.Button(menu_window, text='Exit', padx=100, pady=10, command=exit_program)
    exit_button.grid(row=4, column=0, sticky="ew")
    menu_window.grid_rowconfigure(0, weight=1)
    menu_window.grid_columnconfigure(0, weight=1)

    menu_window.mainloop()


def check_login(login, password):
    """Funkcja sprawdzająca poprawność dnaych uzytych w próbie logowania z danymi znajdującymi się w bazie
    Argument:
        @login(string)
        @password(string)"""
    if sql_query.check_user_in_database(login, password):
        input_name.delete(0, 'end')
        input_password.delete(0, 'end')
        login_window.withdraw()
        show_menu(login)

    else:
        messagebox.showerror("Wrong login or password", "Error")
        input_name.delete(0, 'end')
        input_password.delete(0, 'end')


# Window configuration
login_window = tk.Tk()

login_window.title("AGZ Restaurant")
login_window.iconbitmap(r'..\..\resources\graphics\lg.ico')

login_window.geometry("300x100+300+300")

label_restaurant = tk.Label(login_window, text='AGZ Restaurant')
# Label and entry
label_name = tk.Label(login_window, text="Username", fg="black")
label_password = tk.Label(login_window, text="Password", fg="black")
input_name = tk.Entry(login_window)
input_password = tk.Entry(login_window, show="*")

label_restaurant.grid(row=0, column=0, columnspan=2)
label_name.grid(row=1, column=0, sticky=tk.E)
label_password.grid(row=2, column=0, sticky=tk.E)

input_name.grid(row=1, column=1)
input_password.grid(row=2, column=1)
# Button
login_button = tk.Button(login_window, text="Login",
                         command=lambda: check_login(input_name.get(), input_password.get()))
login_button.grid(row=1, column=3, rowspan=2, padx=15, pady=5)

# menubar
menubar = tk.Menu(login_window)
add_user = tk.Menu(menubar, tearoff=0)

add_user.add_command(label="Admin", command=admin_panel.open_admin_menu)
menubar.add_cascade(label="Menu", menu=add_user)

login_window.config(menu=menubar)
login_window.mainloop()
