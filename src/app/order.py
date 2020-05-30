"""
Modłuł zawierający wszystkie funkcje służące do wykonywania, anulowania oraz kontrolowania zamówień
"""

import random
import time
import tkinter as tk
from tkinter import messagebox

from src.sql import sql_query


def show_menu_window():
    """Funkcja tworząca moduł zamówienia"""

    # FUNCTIONS:

    def make_an_order(list_of_product):
        """funckja przekazująca zapytanie z do bazy danych o utworzenie zamówienia
            @argument lsit_of_product(list)"""

    def check_checkbutton_value():
        """Funkcja sprawdzająca status checkboxes"""
        # Burgers
        if cheeseburger_check_var.get() == 1:
            cheeseburger_entry.configure(state=tk.NORMAL)
        elif cheeseburger_check_var.get() == 0:
            cheeseburger_entry.configure(state=tk.DISABLED)
            cheeseburger_entry_var.set("0")
        if hamburger_check_var.get() == 1:
            hamburger_entry.configure(state=tk.NORMAL)
        elif hamburger_check_var.get() == 0:
            hamburger_entry.configure(state=tk.DISABLED)
            hamburger_entry_var.set("0")
        if vegeburger_check_var.get() == 1:
            vegeburger_entry.configure(state=tk.NORMAL)
        elif vegeburger_check_var.get() == 0:
            vegeburger_entry.configure(state=tk.DISABLED)
            vegeburger_entry_var.set("0")
        # Drinks
        if lemonade_check_var.get() == 1:
            lemonade_entry.configure(state=tk.NORMAL)
        elif lemonade_check_var.get() == 0:
            lemonade_entry.configure(state=tk.DISABLED)
            lemonade_entry_var.set("0")
        if cola_check_var.get() == 1:
            cola_entry.configure(state=tk.NORMAL)
        elif cola_check_var.get() == 0:
            cola_entry.configure(state=tk.DISABLED)
            cola_entry_var.set("0")
        if water_check_var.get() == 1:
            water_entry.configure(state=tk.NORMAL)
        elif water_check_var.get() == 0:
            water_entry.configure(state=tk.DISABLED)
            water_entry_var.set("0")
        if sparkly_water_check_var.get() == 1:
            sparkly_water_entry.configure(state=tk.NORMAL)
        elif sparkly_water_check_var.get() == 0:
            sparkly_water_entry.configure(state=tk.DISABLED)
            sparkly_water_entry_var.set("0")
        if beer_check_var.get() == 1:
            beer_entry.configure(state=tk.NORMAL)
        elif beer_check_var.get() == 0:
            beer_entry.configure(state=tk.DISABLED)
            beer_entry_var.set("0")
        if juice_check_var.get() == 1:
            juice_entry.configure(state=tk.NORMAL)
        elif juice_check_var.get() == 0:
            juice_entry.configure(state=tk.DISABLED)
            juice_entry_var.set("0")
        # Desserts
        if waffles_check_var.get() == 1:
            waffles_entry.configure(state=tk.NORMAL)
        elif waffles_check_var.get() == 0:
            waffles_entry.configure(state=tk.DISABLED)
            waffles_entry_var.set("0")
        if ice_cream_check_var.get() == 1:
            ice_cream_entry.configure(state=tk.NORMAL)
        elif ice_cream_check_var.get() == 0:
            ice_cream_entry.configure(state=tk.DISABLED)
            ice_cream_entry_var.set("0")
        if salad_check_var.get() == 1:
            salad_entry.configure(state=tk.NORMAL)
        elif salad_check_var.get() == 0:
            salad_entry.configure(state=tk.DISABLED)
            salad_entry_var.set("0")
        # Pizza
        if capriciosa_check_var.get() == 1:
            capriciosa_entry.configure(state=tk.NORMAL)
        elif capriciosa_check_var.get() == 0:
            capriciosa_entry.configure(state=tk.DISABLED)
            capriciosa_entry_var.set("0")
        if diavola_check_var.get() == 1:
            diavola_entry.configure(state=tk.NORMAL)
        elif diavola_check_var.get() == 0:
            diavola_entry.configure(state=tk.DISABLED)
            diavola_entry_var.set("0")
        if margherita_check_var.get() == 1:
            margherita_entry.configure(state=tk.NORMAL)
        elif margherita_check_var.get() == 0:
            margherita_entry.configure(state=tk.DISABLED)
            margherita_entry_var.set("0")
        # Additives
        if chips_check_var.get() == 1:
            chips_entry.configure(state=tk.NORMAL)
        elif chips_check_var.get() == 0:
            chips_entry.configure(state=tk.DISABLED)
            chips_entry_var.set("0")
        if rings_check_var.get() == 1:
            rings_entry.configure(state=tk.NORMAL)
        elif rings_check_var.get() == 0:
            rings_entry.configure(state=tk.DISABLED)
            rings_entry_var.set("0")

    def exit_order_menu():
        """Funkcja służąca do zamknięcia panelu z zamówieniami"""

        exit_var = messagebox.askyesno("Quit order", "Do you want to quit?")
        if exit_var > 0:
            order_window.destroy()
            order_window.quit()

    def reset_actual_order():
        """Funkcja służąca do wyczyszczenia tymczasowych danych wprowadzonych jako zamówienie """

        receipt_text.delete("1.0", tk.END)
        total_cost.set("0")
        # Burgers
        cheeseburger_entry_var.set("0")
        hamburger_entry_var.set("0")
        vegeburger_entry_var.set("0")
        cheeseburger_check_var.set("0")
        hamburger_check_var.set("0")
        vegeburger_check_var.set("0")
        cheeseburger_entry.configure(state=tk.DISABLED)
        hamburger_entry.configure(state=tk.DISABLED)
        vegeburger_entry.configure(state=tk.DISABLED)

        # Drinks
        lemonade_entry_var.set("0")
        cola_entry_var.set("0")
        water_entry_var.set("0")
        juice_entry_var.set("0")
        sparkly_water_entry_var.set("0")
        beer_entry_var.set("0")
        lemonade_check_var.set("0")
        cola_check_var.set("0")
        water_check_var.set("0")
        juice_check_var.set("0")
        sparkly_water_check_var.set("0")
        beer_check_var.set("0")
        lemonade_entry.configure(state=tk.DISABLED)
        cola_entry.configure(state=tk.DISABLED)
        water_entry.configure(state=tk.DISABLED)
        juice_entry.configure(state=tk.DISABLED)
        sparkly_water_entry.configure(state=tk.DISABLED)
        beer_entry.configure(state=tk.DISABLED)

        # Desserts
        waffles_entry_var.set("0")
        ice_cream_entry_var.set("0")
        salad_entry_var.set("0")
        waffles_check_var.set("0")
        ice_cream_check_var.set("0")
        salad_check_var.set("0")
        waffles_entry.configure(state=tk.DISABLED)
        ice_cream_entry.configure(state=tk.DISABLED)
        salad_entry.configure(state=tk.DISABLED)

        # Pizza
        capriciosa_entry_var.set("0")
        diavola_entry_var.set("0")
        margherita_entry_var.set("0")
        capriciosa_check_var.set("0")
        diavola_check_var.set("0")
        margherita_check_var.set("0")
        capriciosa_entry.configure(state=tk.DISABLED)
        diavola_entry.configure(state=tk.DISABLED)
        margherita_entry.configure(state=tk.DISABLED)

        # Additives
        chips_entry_var.set("0")
        rings_entry_var.set("0")
        chips_check_var.set("0")
        rings_check_var.set("0")
        chips_entry.configure(state=tk.DISABLED)
        rings_entry.configure(state=tk.DISABLED)

    def calculate_cost_of_order():
        """Funkcja podliczająca wartość aktualnego zamówienia """
        # Burgers
        amount_of_cheeseburger = float(cheeseburger_entry_var.get())
        amount_of_hamburger = float(hamburger_entry_var.get())
        amount_of_vegeburger = float(vegeburger_entry_var.get())
        # Drinks
        amount_of_lemonade = float(lemonade_entry_var.get())
        amount_of_cola = float(cola_entry_var.get())
        amount_of_water = float(water_entry_var.get())
        amount_of_juice = float(juice_entry_var.get())
        amount_of_sparkly_water = float(sparkly_water_entry_var.get())
        amount_of_beer = float(beer_entry_var.get())
        # Desserts
        amount_of_waffles = float(waffles_entry_var.get())
        amount_of_ice_cream = float(ice_cream_entry_var.get())
        amount_of_salad = float(salad_entry_var.get())
        # Pizza
        amount_of_capriciosa = float(capriciosa_entry_var.get())
        amount_of_diavola = float(diavola_entry_var.get())
        amount_of_margherita = float(margherita_entry_var.get())
        # Additives
        amount_of_chips = float(chips_entry_var.get())
        amount_of_rings = float(rings_entry_var.get())

        # Cost of Burgers
        cost_of_burgers = (amount_of_cheeseburger * cheeseburger_price) + (amount_of_hamburger * hamburger_price) + (
                amount_of_vegeburger * vegeburger_price)
        # Cost of Drinks
        cost_of_drinks = (amount_of_lemonade * lemonade_price) + (amount_of_cola * cola_price) + (
                amount_of_water * water_price) + (
                                 amount_of_juice * juice_price) + (amount_of_sparkly_water * sparkly_price) + (
                                 amount_of_beer * beer_price)
        # Cost of desserts
        cost_of_desserts = (amount_of_waffles * waffles_price) + (amount_of_ice_cream * ice_cream_price) + (
                amount_of_salad * salad_price)
        # Cost of pizza
        cost_of_pizza = (amount_of_capriciosa * capricciosa_price) + (amount_of_diavola * diavola_price) + (
                amount_of_margherita * margherita_price)
        # Cost of additives
        cost_of_additives = (amount_of_chips * chips_price) + (amount_of_rings * rings_price)

        # Total cost
        cost_of_order = cost_of_burgers + cost_of_drinks + cost_of_desserts + cost_of_pizza + cost_of_additives
        actual_cost = f"Total cost: {cost_of_order} zł"
        total_cost.set(actual_cost)

    def display_receipt():
        """Funkcja która wyświetla rachunek za zamówienie """

        receipt_text.delete("1.0", tk.END)
        random_x = random.randint(1000, 500890)
        random_ref = str(random_x)
        receipt_ref.set("BILL" + random_ref)

        receipt_text.insert(tk.END, 'Receipt Ref:\t\t\t' + receipt_ref.get() + '\t\t' + date_of_order.get() + "\n")
        receipt_text.insert(tk.END, 'Items\t\t\t\t' + "Cost of Items \n\n")
        # Burgers
        receipt_text.insert(tk.END, 'Cheeseburger:\t\t\t\t\t' + cheeseburger_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Hamburger: \t\t\t\t\t' + hamburger_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Vegeburger: \t\t\t\t\t' + vegeburger_entry_var.get() + "\n")
        # Drinks
        receipt_text.insert(tk.END, 'Lemonade: \t\t\t\t\t' + lemonade_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Cola: \t\t\t\t\t' + cola_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Still water: \t\t\t\t\t' + water_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Sparkly water: \t\t\t\t\t' + sparkly_water_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Orange juice: \t\t\t\t\t' + juice_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Beer: \t\t\t\t\t' + beer_entry_var.get() + "\n")
        # Desserts
        receipt_text.insert(tk.END, 'Waffles:\t\t\t\t\t' + waffles_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Ice cream: \t\t\t\t\t' + ice_cream_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Salad: \t\t\t\t\t' + salad_entry_var.get() + "\n")
        # Pizza
        receipt_text.insert(tk.END, 'Capriciosa:\t\t\t\t\t' + capriciosa_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Diavola: \t\t\t\t\t' + diavola_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Margherita: \t\t\t\t\t' + margherita_entry_var.get() + "\n")
        # Additives
        receipt_text.insert(tk.END, 'Chips:\t\t\t\t\t' + chips_entry_var.get() + "\n")
        receipt_text.insert(tk.END, 'Onion ring: \t\t\t\t\t' + rings_entry_var.get() + "\n")

        calculate_cost_of_order()

        receipt_text.insert(tk.END, "Total Cost:\t\t\t\t\t" + total_cost.get() + "\n")

    def make_list_of_product_to_order():
        """Funckcja która odczytuje ile i jakich produktów zostało zamówionnych a
        następnie wywołująca funkcje która doda zamoówienie do bazy danych """
        product_list = []
        # Burgers
        amount_of_cheeseburger = float(cheeseburger_entry_var.get())
        if amount_of_cheeseburger != 0:
            product_list.append(('Cheeseburger', amount_of_cheeseburger))
        amount_of_hamburger = float(hamburger_entry_var.get())
        if amount_of_hamburger != 0:
            product_list.append(('Hamburger', amount_of_hamburger))
        amount_of_vegeburger = float(vegeburger_entry_var.get())
        if amount_of_cheeseburger != 0:
            product_list.append(('Vegeburger', amount_of_vegeburger))
        # Drinks
        amount_of_lemonade = float(lemonade_entry_var.get())
        if amount_of_lemonade != 0:
            product_list.append(('Lemonade', amount_of_lemonade))
        amount_of_cola = float(cola_entry_var.get())
        if amount_of_cola != 0:
            product_list.append(('Cola', amount_of_cola))
        amount_of_water = float(water_entry_var.get())
        if amount_of_water != 0:
            product_list.append(('Water', amount_of_water))
        amount_of_juice = float(juice_entry_var.get())
        if amount_of_juice != 0:
            product_list.append(('Juice', amount_of_juice))
        amount_of_sparkly_water = float(sparkly_water_entry_var.get())
        if amount_of_sparkly_water != 0:
            product_list.append(('Sparkly water', amount_of_sparkly_water))
        amount_of_beer = float(beer_entry_var.get())
        if amount_of_beer != 0:
            product_list.append(('Beer', amount_of_beer))
        # Desserts
        amount_of_waffles = float(waffles_entry_var.get())
        if amount_of_waffles != 0:
            product_list.append(('Waffles', amount_of_waffles))
        amount_of_ice_cream = float(ice_cream_entry_var.get())
        if amount_of_ice_cream != 0:
            product_list.append(('Ice cream', amount_of_ice_cream))
        amount_of_salad = float(salad_entry_var.get())
        if amount_of_salad != 0:
            product_list.append(('Salad', amount_of_salad))
        # Pizza
        amount_of_capriciosa = float(capriciosa_entry_var.get())
        if amount_of_capriciosa != 0:
            product_list.append(('Capriciosa', amount_of_capriciosa))
        amount_of_diavola = float(diavola_entry_var.get())
        if amount_of_diavola != 0:
            product_list.append(('Diavola', amount_of_diavola))
        amount_of_margherita = float(margherita_entry_var.get())
        if amount_of_margherita != 0:
            product_list.append(('Margherita', amount_of_margherita))
        # Additives
        amount_of_chips = float(chips_entry_var.get())
        if amount_of_chips != 0:
            product_list.append(('Chips', amount_of_chips))
        amount_of_rings = float(rings_entry_var.get())
        if amount_of_rings != 0:
            product_list.append(('Onion rings', amount_of_rings))
        make_an_order(product_list)

    # Window configuration
    order_window = tk.Toplevel()

    order_window.title("AGZ Restaurant")
    order_window.iconbitmap(r'..\..\resources\graphics\lg.ico')

    order_window.geometry("+50+50")

    # Menu frame
    menu_frame = tk.Frame(order_window, bd=1)
    menu_frame.pack(side=tk.LEFT)

    # Receipt frame
    main_receipt_frame = tk.Frame(order_window, bd=1)
    main_receipt_frame.pack(side=tk.RIGHT)

    # title frame
    title_frame = tk.Frame(menu_frame, bd=5)
    title_frame.grid(row=0, columnspan=2)
    title_text = tk.Label(title_frame, font=('arial', 64, 'bold'), text="Menu", bd=9)
    title_text.grid(row=0, columnspan=2)

    # Prices
    price_of_food = sql_query.get_price_of_product()
    cheeseburger_price = [price[1] for price in price_of_food if 'cheeseburger' in price][0]
    hamburger_price = [price[1] for price in price_of_food if 'hamburger' in price][0]
    vegeburger_price = [price[1] for price in price_of_food if 'vegeburger' in price][0]
    lemonade_price = [price[1] for price in price_of_food if 'lemoniada' in price][0]
    cola_price = [price[1] for price in price_of_food if 'cola' in price][0]
    water_price = [price[1] for price in price_of_food if 'woda niegazowana' in price][0]
    juice_price = [price[1] for price in price_of_food if 'sok pomarańczowy' in price][0]
    sparkly_price = [price[1] for price in price_of_food if 'woda gazowana' in price][0]
    beer_price = [price[1] for price in price_of_food if 'piwo' in price][0]
    waffles_price = [price[1] for price in price_of_food if 'gofry' in price][0]
    ice_cream_price = [price[1] for price in price_of_food if 'lody włoskie' in price][0]
    salad_price = [price[1] for price in price_of_food if 'sałatka owocowa' in price][0]
    capricciosa_price = [price[1] for price in price_of_food if 'capricciosa' in price][0]
    diavola_price = [price[1] for price in price_of_food if 'diavola' in price][0]
    margherita_price = [price[1] for price in price_of_food if 'margherita' in price][0]
    chips_price = [price[1] for price in price_of_food if 'frytki' in price][0]
    rings_price = [price[1] for price in price_of_food if 'krążki cebulowe' in price][0]

    # food frame
    burger_frame = tk.Frame(menu_frame, bd=5, relief=tk.RAISED)
    burger_frame.grid(row=1, column=0)

    burger_text = tk.Label(burger_frame, font=('arial', 26, 'bold'), text="BURGER")
    burger_text.grid(sticky="n", columnspan=2)

    # cheeseburger
    cheeseburger_check_var = tk.IntVar()
    cheeseburger_entry_var = tk.StringVar()
    cheeseburger_checkbutton = tk.Checkbutton(burger_frame, font=('arial', 18, 'bold'),
                                              text=f"Cheeseburger {cheeseburger_price}",
                                              variable=cheeseburger_check_var,
                                              onvalue=1, offvalue=0, command=check_checkbutton_value)
    cheeseburger_checkbutton.grid(row=1, column=0, sticky="w")
    cheeseburger_entry = tk.Entry(burger_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                                  state=tk.DISABLED,
                                  textvariable=cheeseburger_entry_var)
    cheeseburger_entry.grid(row=1, column=1)

    # hamburger
    hamburger_check_var = tk.IntVar()
    hamburger_entry_var = tk.StringVar()
    hamburger_checkbutton = tk.Checkbutton(burger_frame, font=('arial', 18, 'bold'),
                                           text=f"Hamburger {hamburger_price}",
                                           variable=hamburger_check_var,
                                           onvalue=1, offvalue=0, command=check_checkbutton_value)
    hamburger_checkbutton.grid(row=2, column=0, sticky="w")
    hamburger_entry = tk.Entry(burger_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                               state=tk.DISABLED,
                               textvariable=hamburger_entry_var)
    hamburger_entry.grid(row=2, column=1)

    # vegeburger
    vegeburger_check_var = tk.IntVar()
    vegeburger_entry_var = tk.StringVar()
    vegeburger_checkbutton = tk.Checkbutton(burger_frame, font=('arial', 18, 'bold'),
                                            text=f"Vegeburger {vegeburger_price}",
                                            variable=vegeburger_check_var,
                                            onvalue=1, offvalue=0, command=check_checkbutton_value)
    vegeburger_checkbutton.grid(row=3, column=0, sticky="w")
    vegeburger_entry = tk.Entry(burger_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                                state=tk.DISABLED,
                                textvariable=vegeburger_entry_var)
    vegeburger_entry.grid(row=3, column=1)

    # drink frame
    drink_frame = tk.Frame(menu_frame, bd=5, relief=tk.RAISED)
    drink_frame.grid(row=2, column=0, rowspan=2)

    drink_text = tk.Label(drink_frame, font=('arial', 26, 'bold'), text="DRINK")
    drink_text.grid(sticky="n", columnspan=2)

    # lemonade
    lemonade_check_var = tk.IntVar()
    lemonade_entry_var = tk.StringVar()
    lemonade_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'), text=f"Lemonade {lemonade_price}",
                                          variable=lemonade_check_var,
                                          onvalue=1, offvalue=0, command=check_checkbutton_value)
    lemonade_checkbutton.grid(row=1, column=0, sticky="w")
    lemonade_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                              state=tk.DISABLED,
                              textvariable=lemonade_entry_var)
    lemonade_entry.grid(row=1, column=1)

    # cola
    cola_check_var = tk.IntVar()
    cola_entry_var = tk.StringVar()
    cola_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'), text=f"Cola {cola_price}",
                                      variable=cola_check_var,
                                      onvalue=1, offvalue=0, command=check_checkbutton_value)
    cola_checkbutton.grid(row=2, column=0, sticky="w")
    cola_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED, state=tk.DISABLED,
                          textvariable=cola_entry_var)
    cola_entry.grid(row=2, column=1)

    # still water
    water_check_var = tk.IntVar()
    water_entry_var = tk.StringVar()
    water_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'), text=f"Still water {water_price}",
                                       variable=water_check_var,
                                       onvalue=1, offvalue=0, command=check_checkbutton_value)
    water_checkbutton.grid(row=3, column=0, sticky="w")
    water_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED, state=tk.DISABLED,
                           textvariable=water_entry_var)
    water_entry.grid(row=3, column=1)

    # beer
    beer_check_var = tk.IntVar()
    beer_entry_var = tk.StringVar()
    beer_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'), text=f"Beer {beer_price}",
                                      variable=beer_check_var,
                                      onvalue=1, offvalue=0, command=check_checkbutton_value)
    beer_checkbutton.grid(row=4, column=0, sticky="w")
    beer_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED, state=tk.DISABLED,
                          textvariable=beer_entry_var)
    beer_entry.grid(row=4, column=1)

    # orange juice
    juice_check_var = tk.IntVar()
    juice_entry_var = tk.StringVar()
    juice_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'), text=f"Orange juice {juice_price}",
                                       variable=juice_check_var,
                                       onvalue=1, offvalue=0, command=check_checkbutton_value)
    juice_checkbutton.grid(row=5, column=0, sticky="w")
    juice_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED, state=tk.DISABLED,
                           textvariable=juice_entry_var)
    juice_entry.grid(row=5, column=1)

    # sparkly water
    sparkly_water_check_var = tk.IntVar()
    sparkly_water_entry_var = tk.StringVar()
    sparkly_water_checkbutton = tk.Checkbutton(drink_frame, font=('arial', 18, 'bold'),
                                               text=f"Sparkly water {sparkly_price}",
                                               variable=sparkly_water_check_var,
                                               onvalue=1, offvalue=0, command=check_checkbutton_value)
    sparkly_water_checkbutton.grid(row=6, column=0, sticky="w")
    sparkly_water_entry = tk.Entry(drink_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                                   state=tk.DISABLED,
                                   textvariable=sparkly_water_entry_var)
    sparkly_water_entry.grid(row=6, column=1)

    # Desserts frame

    desserts_frame = tk.Frame(menu_frame, bd=5, relief=tk.RAISED)
    desserts_frame.grid(row=2, column=1, columnspan=2)

    desserts_text = tk.Label(desserts_frame, font=('arial', 26, 'bold'), text="DESSERTS")
    desserts_text.grid(sticky="n", columnspan=2)

    # Waffles
    waffles_check_var = tk.IntVar()
    waffles_entry_var = tk.StringVar()
    waffles_checkbutton = tk.Checkbutton(desserts_frame, font=('arial', 18, 'bold'), text=f"Waffles {waffles_price}",
                                         variable=waffles_check_var,
                                         onvalue=1, offvalue=0, command=check_checkbutton_value)
    waffles_checkbutton.grid(row=1, column=0, sticky="w")
    waffles_entry = tk.Entry(desserts_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                             state=tk.DISABLED,
                             textvariable=waffles_entry_var)
    waffles_entry.grid(row=1, column=1)

    # Ice cream
    ice_cream_check_var = tk.IntVar()
    ice_cream_entry_var = tk.StringVar()
    ice_cream_checkbutton = tk.Checkbutton(desserts_frame, font=('arial', 18, 'bold'),
                                           text=f"Ice cream {ice_cream_price}",
                                           variable=ice_cream_check_var,
                                           onvalue=1, offvalue=0, command=check_checkbutton_value)
    ice_cream_checkbutton.grid(row=2, column=0, sticky="w")
    ice_cream_entry = tk.Entry(desserts_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                               state=tk.DISABLED,
                               textvariable=ice_cream_entry_var)
    ice_cream_entry.grid(row=2, column=1)

    # salad
    salad_check_var = tk.IntVar()
    salad_entry_var = tk.StringVar()
    salad_checkbutton = tk.Checkbutton(desserts_frame, font=('arial', 18, 'bold'), text=f"Salad {salad_price}",
                                       variable=salad_check_var,
                                       onvalue=1, offvalue=0, command=check_checkbutton_value)
    salad_checkbutton.grid(row=3, column=0, sticky="w")
    salad_entry = tk.Entry(desserts_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                           state=tk.DISABLED,
                           textvariable=salad_entry_var)
    salad_entry.grid(row=3, column=1)

    # Pizza frame
    pizza_frame = tk.Frame(menu_frame, bd=5, relief=tk.RAISED)
    pizza_frame.grid(row=1, column=1)

    pizza_text = tk.Label(pizza_frame, font=('arial', 26, 'bold'), text="PIZZA")
    pizza_text.grid(sticky="n", columnspan=2)

    # capriciosa
    capriciosa_check_var = tk.IntVar()
    capriciosa_entry_var = tk.StringVar()
    capriciosa_checkbutton = tk.Checkbutton(pizza_frame, font=('arial', 18, 'bold'),
                                            text=f"Capriciosa {capricciosa_price}",
                                            variable=capriciosa_check_var,
                                            onvalue=1, offvalue=0, command=check_checkbutton_value)
    capriciosa_checkbutton.grid(row=1, column=0, sticky="w")
    capriciosa_entry = tk.Entry(pizza_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                                state=tk.DISABLED,
                                textvariable=capriciosa_entry_var)
    capriciosa_entry.grid(row=1, column=1)

    # diavola
    diavola_check_var = tk.IntVar()
    diavola_entry_var = tk.StringVar()
    diavola_checkbutton = tk.Checkbutton(pizza_frame, font=('arial', 18, 'bold'), text=f"Diavola {diavola_price}",
                                         variable=diavola_check_var,
                                         onvalue=1, offvalue=0, command=check_checkbutton_value)
    diavola_checkbutton.grid(row=2, column=0, sticky="w")
    diavola_entry = tk.Entry(pizza_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                             state=tk.DISABLED,
                             textvariable=diavola_entry_var)
    diavola_entry.grid(row=2, column=1)

    # MARGHERITA
    margherita_check_var = tk.IntVar()
    margherita_entry_var = tk.StringVar()
    margherita_checkbutton = tk.Checkbutton(pizza_frame, font=('arial', 18, 'bold'),
                                            text=f"Margherita {margherita_price}",
                                            variable=margherita_check_var,
                                            onvalue=1, offvalue=0, command=check_checkbutton_value)
    margherita_checkbutton.grid(row=3, column=0, sticky="w")
    margherita_entry = tk.Entry(pizza_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                                state=tk.DISABLED,
                                textvariable=margherita_entry_var)
    margherita_entry.grid(row=3, column=1)

    # Additives frame
    additives_frame = tk.Frame(menu_frame, bd=5, relief=tk.RAISED)
    additives_frame.grid(row=3, column=1)

    additives_text = tk.Label(additives_frame, font=('arial', 26, 'bold'), text="ADDITIVES")
    additives_text.grid(sticky="n", columnspan=2)

    # chips
    chips_check_var = tk.IntVar()
    chips_entry_var = tk.StringVar()
    chips_checkbutton = tk.Checkbutton(additives_frame, font=('arial', 18, 'bold'), text=f"Chips {chips_price}",
                                       variable=chips_check_var,
                                       onvalue=1, offvalue=0, command=check_checkbutton_value)
    chips_checkbutton.grid(row=1, column=0, sticky="w")
    chips_entry = tk.Entry(additives_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                           state=tk.DISABLED,
                           textvariable=chips_entry_var)
    chips_entry.grid(row=1, column=1)

    # rings
    rings_check_var = tk.IntVar()
    rings_entry_var = tk.StringVar()
    rings_checkbutton = tk.Checkbutton(additives_frame, font=('arial', 18, 'bold'), text=f"Onion rings {rings_price}",
                                       variable=rings_check_var,
                                       onvalue=1, offvalue=0, command=check_checkbutton_value)
    rings_checkbutton.grid(row=2, column=0, sticky="w")
    rings_entry = tk.Entry(additives_frame, font=('arial', 16, 'bold'), width=3, bd=4, relief=tk.RAISED,
                           state=tk.DISABLED,
                           textvariable=rings_entry_var)
    rings_entry.grid(row=2, column=1)

    # receipt frame
    receipt_frame = tk.Frame(main_receipt_frame, bd=5, relief=tk.RAISED)
    receipt_frame.grid(row=1, column=0)
    receipt_label = tk.Label(receipt_frame, font=('arial', 26, 'bold'), text="RECEIPT")
    receipt_label.grid(sticky="n", columnspan=3)

    receipt_ref = tk.StringVar()
    date_of_order = tk.StringVar()
    total_cost = tk.StringVar()
    date_of_order.set(time.strftime("%d/%m/%y"))

    receipt_text = tk.Text(receipt_frame, bd=8, font=('arial', 11, 'bold'))

    receipt_text.grid()

    # button frame
    button_frame = tk.Frame(main_receipt_frame, bd=5, relief=tk.RAISED)
    button_frame.grid(row=2, columnspan=3)
    exit_button = tk.Button(button_frame, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                            text="Back", command=exit_order_menu)
    exit_button.grid(row=1, column=0)

    reset_button = tk.Button(button_frame, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                             text="Reset", command=reset_actual_order)
    reset_button.grid(row=1, column=1)

    order_button = tk.Button(button_frame, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                             text="Receipt", command=display_receipt)
    order_button.grid(row=1, column=2)

    total_button = tk.Button(button_frame, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                             text="Order", command=make_list_of_product_to_order)
    total_button.grid(row=1, column=3)

    order_window.mainloop()
