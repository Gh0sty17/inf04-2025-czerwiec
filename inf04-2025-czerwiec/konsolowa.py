import random


class Loteria:
    def __init__(self, liczba_losowan):
        self.liczba_losowan = liczba_losowan
        self.losowania = []

    def wypelnij_losowania(self):
        for _ in range(self.liczba_losowan):
            zestaw = random.sample(range(1, 50), 6)
            self.losowania.append(zestaw)

    def wyswietl_losowania(self):
        print("\nZestawy wylosowanych liczb:")

        for numer, zestaw in enumerate(self.losowania, start=1):
            zestaw.sort()
            print(f"Losowanie {numer}: {' '.join(map(str, zestaw))}")

    def zlicz_wystapienia(self):
        wystapienia = [0] * 50

        for zestaw in self.losowania:
            for liczba in zestaw:
                wystapienia[liczba] += 1

        return wystapienia

    def wyswietl_wystapienia(self):
        wystapienia = self.zlicz_wystapienia()

        print("\nWystąpienia liczb:")

        for liczba in range(1, 50):
            print(f"Wystąpienia liczby {liczba}: {wystapienia[liczba]}")


def main():
    print("LOTERIA LICZBOWA")
    print("================")

    while True:
        try:
            liczba_losowan = int(input("Ile wygenerować losowań? "))

            if liczba_losowan > 0:
                break

            print("Podaj liczbę większą od 0.")

        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")

    loteria = Loteria(liczba_losowan)

    loteria.wypelnij_losowania()
    loteria.wyswietl_losowania()
    loteria.wyswietl_wystapienia()


if __name__ == "__main__":
    main()