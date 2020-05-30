"""
Moduł zawierający wszyskie funkcje służące do komunikacji oraz modyfikacji z bazą danych aplikacji
"""

import sqlite3
from tkinter import messagebox


def check_login_is_free():
    """Funkcja zwracająca listę loginów uzytkowników aktualnie znajdującyhc się w bazie danych
        @return (list)"""
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute("""
        SELECT login FROM workers
        """)

    list_of_user = cur.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    return list_of_user


def create_list_of_users():
    """Funkcja zwracająca liste aktualnych użytkowników w bazie dancyh w kolejności alfabetycznej
        @return (list)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute("""SELECT * FROM workers ORDER BY first_name""")
    list_of_users = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return list_of_users


def add_user_to_database(first_name, last_name, login, password, role):
    """Funkcja która dodaje użytkownika o podanych argumentach do bazy danych
        Argumenty:
            @first_name(string)
            @last_name(string)
            @login(string)
            @password(string)
            @role(char: 'P', 'M', 'K')"""
    # check what role
    if role == 1:
        role = 'P'
    elif role == 2:
        role = 'K'
    elif role == 3:
        role = 'M'
    else:
        role = None

    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    list_of_user = check_login_is_free()
    for user_login in list_of_user:
        if user_login[0] == login:
            messagebox.showerror("Error", "There is a user with this login")
            return
    if len(first_name) == 0:
        messagebox.showerror("Error", "Field first_name is empty")
        return
    elif len(last_name) == 0:
        messagebox.showerror("Error", "Field last_name is empty")
        return
    elif len(login) == 0:
        messagebox.showerror("Error", "Field login is empty")
        return
    elif len(password) == 0:
        messagebox.showerror("Error", "Field password is empty")
        return

    cur.execute("INSERT INTO workers VALUES (Null, :f_name, :l_name, :log, :passwd, :role)",
                {
                    'f_name': first_name,
                    'l_name': last_name,
                    'log': login,
                    'passwd': password,
                    'role': role
                })
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    messagebox.showinfo("User added", "You added user")
    return


def delete_user_from_database(login):
    """Funkcja usuwająca użytkownika o zadanym loginie z bazy danych
        Argument
            @login(string)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    # Create table
    list_of_user = check_login_is_free()
    for user_login in list_of_user:
        if user_login[0] == login:
            cur.execute("DELETE from workers WHERE login='{}'".format(login))
            messagebox.showinfo("Delete", "Successful deleted user")
            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()
            return
    if len(login) == 0:
        messagebox.showerror("Error", "Field login is empty")
        return

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    messagebox.showerror("Error", "There isn't user with this login")
    return


def check_user_in_database(login, password):
    """Funkcja sprawdzająca poprawność danych przekazanych przez argumenty
       z tymi znajdującymi sie w bazie dnaych
       Zwraca ona prawdę jeżeli dane są prawidłowe a fałsz w przeciwnym wypadku
       Argumenty:
            @login(string)
            @password(string)
        Return:
            @(boolean)
    """
    conn = sqlite3.connect('workers_db.db')

    # create cursor
    cur = conn.cursor()

    cur.execute("""
        SELECT login, password FROM workers
        """)

    users = cur.fetchall()
    for user in users:
        if user[0] == login and user[1] == password:
            # Commit Changes
            conn.commit()

            # Close Connection
            conn.close()
            return True

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    return False


def get_name_actual_employee(login):
    """Funkcja która zwraca dane personalne użytkownika o przesłanym w argumencie loginie
        Argument:
            @login(string)
        return:
            @personality_actual_employee(string)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute("""SELECT first_name, last_name FROM workers WHERE login='{}'""".format(login))
    actual_employee = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    personality_actual_employee = str(actual_employee[0][0] + " " + actual_employee[0][1])

    return personality_actual_employee


def get_id_actual_employee(login):
    """Funkcja która zwraca id  użytkownika o przesłanym w argumencie loginie
        Argument:
            @login(string)
        Return:
            @actual_employee(integer)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute("""SELECT worker_id FROM workers WHERE login='{}'""".format(login))
    actual_employee = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return actual_employee


def add_reservation_to_database(number_of_people, date, worker_id, first_name, last_name):
    """Funkcja która dodaje rezerwacje do bazy danych
        Argumenty:
            @number_of_people(integer)
            @date(datatime)
            @worker_id(integer)
            @first_name(string)
            @last_name(string)
        Return:
            @reservation_id(integer)"""
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    # book table
    cur.execute("INSERT INTO reservation VALUES (Null, :amount_of_people, :data,  :worker_id, :first_name, :last_name)",
                {
                    'amount_of_people': number_of_people,
                    'data': date,
                    'worker_id': worker_id,
                    'first_name': first_name,
                    'last_name': last_name,
                })

    # Commit Changes
    conn.commit()

    cur.execute(f"""SELECT reservation_id from reservation
                    WHERE number_of_people = {number_of_people} AND first_name = '{first_name}' AND last_name = '{last_name}'""")
    reservation_id = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    return reservation_id


def get_all_reservation():
    """Funkcja która zwraca wszystkie rezerwacje z bazy danych
        @return all_reservation(list of tuplets)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute("""SELECT * FROM reservation""")
    all_reservation = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return all_reservation


def delete_old_reservation(actual_date):
    """Funkcja która usuwa rezerwacje które mineły z bazy danych
        Argumenty:
            @actual_date(datatime)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()

    cur.execute(f"""delete from reservation where data < {actual_date}""")
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


def delete_reservation(list_of_reservation):
    """Funkcja która usuwa rezerwacje z bazy danych oraz w tabeli tables ustawia reservation_id na wartość NULL
        Argumenty:
            @list_of_reservation(list)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()
    for reservation in list_of_reservation:
        f_name = reservation.split()[0]
        l_name = reservation.split()[1]
        cur.execute(f"""UPDATE tables
                        SET reservation_id = NULL
                        WHERE table_id = (SELECT  table_id
                                          FROM reservation INNER JOIN tables
                                          ON reservation.reservation_id = tables.reservation_id
                                          WHERE reservation.first_name = '{f_name}' AND reservation.last_name = '{l_name}')""")
        conn.commit()
        cur.execute(f"""delete FROM reservation WHERE first_name='{f_name}' AND last_name='{l_name}'""")
        # Commit Changes
        conn.commit()
    # Close Connection
    conn.close()


def get_free_table(amount_of_people):
    """Funkcja która zwraca index pierwszego stolika który pomieści zadaną ilośc osób
        Argumenty:
            @amount_of_people(integer)
        Return:
            @table_id(integer)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()
    cur.execute(f"""SELECT table_id FROM tables
                    WHERE number_of_people = {amount_of_people} and reservation_id is NULL
                    ORDER BY table_id ASC
                    LIMIT 1""")

    first_table = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    return first_table


def add_reservation_to_table(reservation_id, table_id):
    """Funkcja w rekordzie danego stolika dodaje id_rezerwacji
        Argumenty:
            @reservation_id(integer)
            @table_id(integer)"""
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()
    cur.execute(f"""UPDATE tables
                    SET reservation_id = {reservation_id}
                    WHERE table_id = {table_id}""")

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()


def get_price_of_product():
    """Funkcja która pobiera ceny produktów z bazy danych
        @return: list
    """
    # create database
    conn = sqlite3.connect('workers_db.db')
    # create cursor
    cur = conn.cursor()
    cur.execute(f"""SELECT name, price from product""")
    price = cur.fetchall()
    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()
    return price
