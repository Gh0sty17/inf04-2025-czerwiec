import tkinter as tk


def zmien_kolor(event=None):
    czerwony = suwak_r.get()
    zielony = suwak_g.get()
    niebieski = suwak_b.get()

    kolor = f"#{czerwony:02X}{zielony:02X}{niebieski:02X}"

    duzy_prostokat.config(bg=kolor)

    wartosc_r.config(text=str(czerwony))
    wartosc_g.config(text=str(zielony))
    wartosc_b.config(text=str(niebieski))


def pobierz_kolor():
    czerwony = suwak_r.get()
    zielony = suwak_g.get()
    niebieski = suwak_b.get()

    kolor = f"#{czerwony:02X}{zielony:02X}{niebieski:02X}"

    maly_prostokat.config(bg=kolor)
    pobrany_kolor.config(
        text=f"{czerwony}, {zielony}, {niebieski}"
    )


okno = tk.Tk()
okno.title("Wzornik kolorów RGB. Wykonał 123")
okno.geometry("500x500")
okno.configure(bg="#FFF8DC")


duzy_prostokat = tk.Frame(
    okno,
    width=400,
    height=150,
    bg="white"
)
duzy_prostokat.pack(pady=20)
duzy_prostokat.pack_propagate(False)


opis = tk.Label(
    okno,
    text="Dobierz kolor suwakami i zapisz przyciskiem:",
    bg="#FFF8DC",
    font=("Arial", 11)
)
opis.pack(pady=5)


ramka_suwakow = tk.Frame(okno, bg="#FFF8DC")
ramka_suwakow.pack(pady=10)


# Suwak R
etykieta_r = tk.Label(
    ramka_suwakow,
    text="R",
    bg="#FFF8DC",
    font=("Arial", 11, "bold")
)
etykieta_r.grid(row=0, column=0, padx=5)

suwak_r = tk.Scale(
    ramka_suwakow,
    from_=0,
    to=255,
    orient=tk.HORIZONTAL,
    length=300,
    command=zmien_kolor
)
suwak_r.set(255)
suwak_r.grid(row=0, column=1)

wartosc_r = tk.Label(
    ramka_suwakow,
    text="255",
    bg="#FFF8DC",
    width=4
)
wartosc_r.grid(row=0, column=2)


# Suwak G
etykieta_g = tk.Label(
    ramka_suwakow,
    text="G",
    bg="#FFF8DC",
    font=("Arial", 11, "bold")
)
etykieta_g.grid(row=1, column=0, padx=5)

suwak_g = tk.Scale(
    ramka_suwakow,
    from_=0,
    to=255,
    orient=tk.HORIZONTAL,
    length=300,
    command=zmien_kolor
)
suwak_g.set(255)
suwak_g.grid(row=1, column=1)

wartosc_g = tk.Label(
    ramka_suwakow,
    text="255",
    bg="#FFF8DC",
    width=4
)
wartosc_g.grid(row=1, column=2)


# Suwak B
etykieta_b = tk.Label(
    ramka_suwakow,
    text="B",
    bg="#FFF8DC",
    font=("Arial", 11, "bold")
)
etykieta_b.grid(row=2, column=0, padx=5)

suwak_b = tk.Scale(
    ramka_suwakow,
    from_=0,
    to=255,
    orient=tk.HORIZONTAL,
    length=300,
    command=zmien_kolor
)
suwak_b.set(255)
suwak_b.grid(row=2, column=1)

wartosc_b = tk.Label(
    ramka_suwakow,
    text="255",
    bg="#FFF8DC",
    width=4
)
wartosc_b.grid(row=2, column=2)


# Przycisk POBIERZ
przycisk = tk.Button(
    okno,
    text="Pobierz",
    command=pobierz_kolor,
    width=15,
    bg="#CD853F",
    activebackground="#CD853F"
)
przycisk.pack(pady=15)


# Mały prostokąt
maly_prostokat = tk.Label(
    okno,
    text="",
    bg="white",
    width=30,
    height=3
)
maly_prostokat.pack()

pobrany_kolor = tk.Label(
    okno,
    text="255, 255, 255",
    bg="white",
    width=30
)
pobrany_kolor.place(
    relx=0.5,
    rely=0.85,
    anchor="center"
)


okno.mainloop()