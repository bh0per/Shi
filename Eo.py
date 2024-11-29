import tkinter as tk
from tkinter import messagebox

# Funkcje dla przycisków
def akcja1():
    messagebox.showinfo("Akcja 1", "Pierwszy wybór zrobiony!")

def akcja2():
    messagebox.showinfo("Akcja 2", "Drugi wybór zrobiony!")

def akcja3():
    messagebox.showinfo("Akcja 3", "Trzeci wybór zrobiony!")

def akcja4():
    messagebox.showinfo("Akcja 4", "Czwarty wybór zrobiony!")

def akcja5():
    messagebox.showinfo("Akcja 5", "Piąty wybór zrobiony!")

def akcja6():
    messagebox.showinfo("Akcja 6", "Szósty wybór zrobiony!")

def akcja7():
    messagebox.showinfo("Akcja 7", "Siódmy wybór zrobiony!")

def akcja8():
    messagebox.showinfo("Akcja 8", "Ósmy wybór zrobiony!")

def akcja9():
    messagebox.showinfo("Akcja 9", "Dziewiąty wybór zrobiony!")

def akcja10():
    messagebox.showinfo("Akcja 10", "Dziesiąty wybór zrobiony!")

# Tworzenie głównego okna
okno = tk.Tk()
okno.title("Dojebane GUI z 10 wyborami")
okno.geometry("400x400")

# Dodanie przycisków
przyciski = [
    ("Wybór 1", akcja1),
    ("Wybór 2", akcja2),
    ("Wybór 3", akcja3),
    ("Wybór 4", akcja4),
    ("Wybór 5", akcja5),
    ("Wybór 6", akcja6),
    ("Wybór 7", akcja7),
    ("Wybór 8", akcja8),
    ("Wybór 9", akcja9),
    ("Wybór 10", akcja10),
]

for tekst, akcja in przyciski:
    przycisk = tk.Button(okno, text=tekst, command=akcja, width=20, height=2)
    przycisk.pack(pady=5)

# Uruchomienie pętli głównej
okno.mainloop()
