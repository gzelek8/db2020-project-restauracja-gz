# RESTAURACJA
Tematem naszego projektu jest utowrzenie bazy danych oraz aplikacji, która może zostać wykorzystana przez pracowników do obsługi w restauracji. Aplikacja umożliwia tworzenie zamówień oraz ustawianie rezerwacji stolików w restauracji. Pracownicy w zależności od stanowiska mają różny dostęp do opcji aplikacji.

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
|:---------------:|:-------:|:--------:|:-------:|:-----:|:--------------:|
| Adam Żarczyński |  WIMiIP |    IS    |    4    |   4   |    2019/2020   |
|  Grzegorz Zelek |  WIMiIP |    IS    |    4    |   4   |    2019/2020   |

## Projekt bazy danych
![alt]()


## Implementacja zapytań SQL
1. Zwracanie listy loginów użytkowników aktualnie znajdujących się w bazie danych.
```
SELECT login FROM workers
```

2. Zwracanie listy aktualnych użytkowników w bazie dancyh w kolejności alfabetycznej.
```
SELECT * FROM workers ORDER BY first_name
```

3. Dodawanie użytkownika o podanych argumentach do bazy danych.
```
INSERT INTO workers VALUES (Null, :f_name, :l_name, :log, :passwd, :role)
```

4. Usuwanie użytkownika o zadanym loginie z bazy danych.
```
DELETE FROM workers WHERE login='{}'
```

5. Poprzez zwracanie listy loginów i haseł sprawdzamy poprawność danych przekazanych przez argumenty podczas logogwania z tymi znajdującymi sie w bazie dnaych. Zwraca ona prawdę jeżeli dane są prawidłowe, a fałsz w przeciwnym wypadku.
```
SELECT login, password FROM workers
```

6. Zwracanie danych personalnych użytkownika o przesłanym w argumencie loginie.
```
SELECT first_name, last_name FROM workers WHERE login='{}'
```

7. Zwracanie id użytkownika o przesłanym w argumencie loginie.
```
SELECT worker_id FROM workers WHERE login='{}'
```

8. Zwracanie roli użytkownika o przesłanym w argumencie loginie.
```
SELECT role FROM workers WHERE login='{login}'
```

9. Dodanie rezerwacji do bazy danych.
```
INSERT INTO reservation VALUES (Null, :amount_of_people, :data,  :worker_id, :first_name, :last_name)
```

10. Zwracanie rezerwacji o podanych argumentach.
```
SELECT reservation_id from reservation
                    WHERE number_of_people = {number_of_people} AND first_name = '{first_name}' AND last_name = '{last_name}'
```

11. Zwracanie wszystkich rezerwacji z bazy danych.
```
SELECT * FROM reservation
```

12. Usuwanie rezerwacji które mineły z bazy danych.
```
DELETE FROM reservation WHERE data < {actual_date}
```

13. Usuwanie rezerwacji z bazy danych oraz w tabeli tables ustawienie reservation_id na wartość NULL.
```
UPDATE tables
                        SET reservation_id = NULL
                        WHERE table_id = (SELECT  table_id
                                          FROM reservation INNER JOIN tables
                                          ON reservation.reservation_id = tables.reservation_id
                                          WHERE reservation.first_name = '{f_name}' AND reservation.last_name = '{l_name}')
                                          
                                          
DELETE FROM reservation WHERE first_name='{f_name}' AND last_name='{l_name}'
```

14. Zwracanie indexu pierwszego stolika który pomieści zadaną ilośc osób.
```
SELECT table_id FROM tables
                    WHERE number_of_people = {amount_of_people} and reservation_id is NULL
                    ORDER BY table_id ASC
                    LIMIT 1
```

15. Dodanie w rekordzie danego stolika id_rezerwacji.
```
UPDATE tables
                    SET reservation_id = {reservation_id}
                    WHERE table_id = {table_id}
```

16. Pobranie ceny produktów z bazy danych
```
SELECT name, price FROM product
```

17. Dodanie zamówienia do bazy danych (wymaga dodania również encji product_order)
```
INSERT INTO orders VALUES (Null, :table_id,  :discount, :worker_id)


INSERT INTO product_order VALUES ( :amount, :order_id, :name)
```

18. Zwracanie listy wszystkich aktualnych zamówień
```
SELECT order_id, name, amount FROM product_order
                    order by order_id
```

19. Usuwanie zamówienia od podanym id z bazy danych
```
DELETE FROM product_order
                    WHERE order_id={order_id}
```

## Aplikacja
opis

### Przykładowe funkcje użyte w aplikacji
#### Obsługa rezerwacji.

1. Funkcja umożliwiająca dodanie rezerwacji do bazy.
```
def add_reservation_to_database(number_of_people, date, worker_id, first_name, last_name):
    """
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
```

2. Funkcja usuwająca stare rezerwacje.
```
def delete_old_reservation(actual_date):
    """
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
```

3. Funkcja usuwająca rezerwacje z bazy danych i ustawiająca w tabeli tables reservation_id na wartość NULL 
```
def delete_reservation(list_of_reservation):
    """
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
```

## Dodatkowe uwagi
