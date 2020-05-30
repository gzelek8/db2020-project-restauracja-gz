"""
Moduł zawierający wszystkie metody wykorzystywane przez administratora aplikacji
"""

import tkinter as tk
from tkinter import messagebox

from src.app import var
from src.sql import sql_query


def open_admin_menu():
    """Funkcja tworząca panel do logowania dla administratora"""

    def add_user():
        """Funkcja ,dzięki której można dodać użytkownika do aplikacji"""
        for widget in admin_menu.winfo_children():
            widget.destroy()
        # label
        first_name_label = tk.Label(admin_menu, text="First Name", fg="black")
        first_name_label.grid(row=1, column=0)

        last_name_label = tk.Label(admin_menu, text="Last Name", fg="black")
        last_name_label.grid(row=2, column=0)

        login_label = tk.Label(admin_menu, text="Login", fg="black")
        login_label.grid(row=3, column=0)

        password_label = tk.Label(admin_menu, text="Password", fg="black")
        password_label.grid(row=4, column=0)

        # entry
        input_first_name = tk.Entry(admin_menu)
        input_first_name.grid(row=1, column=1)

        input_last_name = tk.Entry(admin_menu)
        input_last_name.grid(row=2, column=1)

        input_login = tk.Entry(admin_menu)
        input_login.grid(row=3, column=1)

        input_password = tk.Entry(admin_menu, show="*", )
        input_password.grid(row=4, column=1)

        # Radiobutton for role
        role_var = tk.IntVar()

        role_w = tk.Radiobutton(admin_menu, text="Worker", variable=role_var, value=1)
        role_k = tk.Radiobutton(admin_menu, text="Chief", variable=role_var, value=2)
        role_m = tk.Radiobutton(admin_menu, text="Manager", variable=role_var, value=3)
        role_w.grid(row=5, column=0)
        role_k.grid(row=5, column=1)
        role_m.grid(row=5, column=2)

        # button
        # add_button służy do wywołania z modułu sql_query.py funkcji
        # zajmującej sie faktycznym dodaniem użytkownika do bazy danych
        add_button = tk.Button(admin_menu, text="Add",
                               command=lambda: sql_query.add_user_to_database(input_first_name.get(),
                                                                              input_last_name.get(),
                                                                              input_login.get(),
                                                                              input_password.get(), role_var.get()))
        add_button.grid(row=6, column=1)
        # back_button służy do przywrócenia poprzedniego okna
        back_button = tk.Button(admin_menu, text="Back", command=create_window)
        back_button.grid(row=6, column=0)

    def delete_user():
        """Funkcja ,dzięki której można usunąć użytkownika z aplikacji"""
        for widget in admin_menu.winfo_children():
            widget.destroy()
        # label
        first_name_label = tk.Label(admin_menu, text="User login", fg="black")
        first_name_label.grid(row=1, column=0)

        # entry
        input_login = tk.Entry(admin_menu)
        input_login.grid(row=1, column=1)

        # button
        # add_button służy do wywołania z modułu sql_query.py funkcji
        # zajmującej sie faktycznym usunięciem użytkownika z bazy danych
        add_button = tk.Button(admin_menu, text="Delete",
                               command=lambda: sql_query.delete_user_from_database(input_login.get()))
        add_button.grid(row=2, column=1)
        # back_button służy do przywrócenia poprzedniego okna
        back_button = tk.Button(admin_menu, text="Back", command=create_window)
        back_button.grid(row=2, column=0)

    def create_window():
        """Funckja która po pomyślnym zalogowaniu się administratora wyświetla panel z dostępnymi opcjami"""
        for widget in admin_menu.winfo_children():
            widget.destroy()

        # Buttons
        add_user_button = tk.Button(admin_menu, text="Add User", fg="black", command=add_user)
        delete_user_button = tk.Button(admin_menu, text="Delete User", fg="black", command=delete_user)
        back_button = tk.Button(admin_menu, text="Back", fg='black', command=lambda: admin_menu.destroy())
        add_user_button.grid(row=1, column=0)
        delete_user_button.grid(row=2, column=0)
        back_button.grid(row=3, column=0)

        # List of users -  pole tekstowe wyświetlające aktualnych użytkowników
        list_of_users = sql_query.create_list_of_users()

        list_of_users_text = tk.Text(admin_menu)
        for user in list_of_users:
            list_of_users_text.insert(tk.END, user[1] + '\t' + user[2] + '\t' + user[3] + '\t' + user[4] + '\t' + user[
                5] + '\n')
        list_of_users_text.grid(row=0, column=0)
        list_of_users_text.configure(state='disabled')

    def check_admin_password():
        """Funkcja służąca do sprawdzenia poprawnności wprowadzonego hasła przez administratora"""
        if input_admin_password.get() == var.ADMIN_PASSWORD:
            create_window()

        else:
            messagebox.showerror("Wrong login or password", "Error")

    # Window configuration
    admin_menu = tk.Toplevel()
    admin_menu.title("AGZ Restaurant")
    admin_menu.iconbitmap(r'..\..\resources\graphics\lg.ico')

    admin_menu.geometry("+100+100")
    admin_password_label = tk.Label(admin_menu, text="Password", fg="black")
    input_admin_password = tk.Entry(admin_menu, show="*", )
    admin_password_label.grid(row=1, column=0, sticky=tk.E)
    input_admin_password.grid(row=1, column=1)
    entry_button = tk.Button(admin_menu, text="Login", command=check_admin_password)
    entry_button.grid(row=1, column=3, rowspan=2, padx=15, pady=5)
    admin_menu.mainloop()
