"""
Modłuł zawierający wszystkie funkcje służące do wykonywania, anulowania oraz kontrolowania rezerwacji
"""
import datetime
import tkinter as tk
from tkinter import messagebox

from tkcalendar import Calendar

from src.sql import sql_query


def calendar(actual_worker):
    """Funkcja tworząca panel do z rezerwacjami
        Argument:
            actual_worker(string)"""

    def show_reservation_on_calendar():
        """Funkcja która korzysta z funkcji zwracającej listę rezerwacji a następnie dodaje ją do kalendarza"""
        all_reservation = sql_query.get_all_reservation()
        for reservation in all_reservation:
            date_of_reservation = datetime.datetime.strptime(reservation[2], '%Y-%m-%d')
            cal.calevent_create(date_of_reservation, text=str(reservation[4] + " " + reservation[5]))

    def book_table():
        """Funkcja służąca do dodanie konktretnej rezerwacji do systemu"""

        def accept_date():
            """Funkcja wyświetlająca poprawność dodania rezerwacji w konkretnym terminie"""
            table_id = sql_query.get_free_table(var.get())
            if table_id:
                date_of_reservation = cal.selection_get()
                cal.calevent_create(date_of_reservation, text=str(first_name.get() + " " + last_name.get()))
                id_worker = sql_query.get_id_actual_employee(actual_worker)
                messagebox.showinfo("Success", "You added a reservation")
                reservation_id = sql_query.add_reservation_to_database(var.get(), date_of_reservation, id_worker[0][0],
                                                                       first_name.get(),
                                                                       last_name.get())
                sql_query.add_reservation_to_table(reservation_id[0][0], table_id[0][0])
                input_reservation.destroy()
            else:
                messagebox.showinfo("Not free table", "Not free table")

        # New window
        input_reservation = tk.Toplevel()

        # Label
        tk.Label(input_reservation, text="First Name").grid(row=0, column=0)
        tk.Label(input_reservation, text="Last Name").grid(row=1, column=0)

        # Entry
        first_name = tk.Entry(input_reservation)
        first_name.grid(row=0, column=1)
        last_name = tk.Entry(input_reservation)
        last_name.grid(row=1, column=1)

        var = tk.IntVar()  # Zmienna zapamiętująca pojemnośc wybranego stolika

        # Radio Buttons -  możliwość wyboru wielkości stolika
        one_person_table = tk.Radiobutton(input_reservation, text="One person table", variable=var, value=1)
        one_person_table.grid(row=2, column=0)
        two_person_table = tk.Radiobutton(input_reservation, text="Two person table", variable=var, value=2)
        two_person_table.grid(row=3, column=0)
        three_person_table = tk.Radiobutton(input_reservation, text="Three person table", variable=var, value=3)
        three_person_table.grid(row=4, column=0)
        four_person_table = tk.Radiobutton(input_reservation, text="Four person table", variable=var, value=4)
        four_person_table.grid(row=5, column=0)
        five_person_table = tk.Radiobutton(input_reservation, text="five person table", variable=var, value=5)
        five_person_table.grid(row=6, column=0)
        six_person_table = tk.Radiobutton(input_reservation, text="Six person table", variable=var, value=6)
        six_person_table.grid(row=7, column=0)

        tk.Button(input_reservation, text="Book", command=accept_date).grid(row=2, column=1, rowspan=6, columnspan=2)
        input_reservation.mainloop()

    def cancel_table():
        """Funkcja służaca do usunięcia rezerwacji z systemu"""

        def cancel_reservation():
            """funkcja która usuwa zaznaczone rezerwacje z kalendarza"""
            index_of_reservation = list_of_reservation.curselection()
            list_of_reservation_to_delete = []
            if index_of_reservation:
                for index in index_of_reservation:
                    list_of_reservation_to_delete.append(list_of_reservation.get(index))
                delete_window.destroy()
                messagebox.showinfo("Success", "Deleted reservation")

                sql_query.delete_reservation(list_of_reservation_to_delete)
                cal.calevent_remove(event_id[0])
            else:
                messagebox.showwarning("Error", "No mark reservation")

        try:
            event_id = cal.get_calevents(cal.selection_get())
            if event_id:
                # New window
                delete_window = tk.Toplevel()
                list_of_reservation = tk.Listbox(delete_window, selectmode='multiple')
                tk.Button(delete_window, text="Cancel", command=cancel_reservation).grid(row=1, column=0)
                for counter, event in enumerate(event_id):
                    list_of_reservation.insert(counter, cal.calevent_cget(event, "text"))

                list_of_reservation.grid(row=0, column=0)
                delete_window.mainloop()

            else:
                messagebox.showwarning("Empty", "This date is already free")
        except:
            messagebox.showwarning("Empty", "This date is already free")

    def print_reservation():
        """Funkcja służąca do wyświetlenia danej rezerwacji"""
        try:
            event_id = cal.get_calevents(cal.selection_get())
            if event_id:
                reservation_data = []
                for event in event_id:
                    reservation_data.append(cal.calevent_cget(event, "text"))
                messagebox.showinfo("Who's reservation?", reservation_data)
            else:
                messagebox.showwarning("Empty", "This date is free")
        except:
            messagebox.showwarning("Empty", "This date is free")

    # Window configuration
    root = tk.Tk()
    root.title("AGZ Restaurant")
    root.iconbitmap(r'..\..\resources\graphics\lg.ico')
    cal = Calendar(root, selectmode='day', selectbackground='red', normalbackground='yellow')

    # Delete old reservation
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    sql_query.delete_old_reservation(date)

    # Fill calendar
    show_reservation_on_calendar()

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    # Buttons
    tk.Button(root, text="Book", command=book_table).pack()
    tk.Button(root, text="Cancel", command=cancel_table).pack()
    tk.Button(root, text="Print", command=print_reservation).pack()
    tk.Button(root, text="Exit", command=lambda: root.destroy()).pack()

    root.mainloop()
