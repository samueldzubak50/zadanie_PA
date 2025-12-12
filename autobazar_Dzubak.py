# Vytvorte program, ktorý umožní spravovať zoznam vozidiel na predaj. Umožní použivateľov nahrávať nové vozidla a prezerať si zoznam uložených vozidiel.


class Auto:
    def __init__(self, znacka, model, rok, cena):
        self.znacka = znacka
        self.model = model
        self.rok = rok
        self.cena = cena

    def __str__(self):
        return (f"\nVozidlo: {self.znacka} {self.model} \nRok výroby: {self.rok} \nCena: {self.cena} €") # výpis vozidla ako ho bude vypisovať v zozname
    
def main():
    auta = [] # zoznam vozidiel

    while True:
        print("\nSpráva vozidiel") # menu programu, kde nás po prvej a druhej intrakcií bude vraciať
        print("\n1. - Pridať vozidlo")
        print("2. - Zobraziť vozidla na predaj.")
        print("3. - Koniec operácie.")
        
        vyber = input("\nVýber možnosť: ")

        if vyber == "1": # po zvolení prvej možnosti nám program bude vyhadzovať špecifikácie, ktorými budeme zapisovať o aké auto ide
            znacka = input("\nZadaj značku vozidla: ")
            model = input ("Zadaj model vozidla: ")
            rok = int(input("Zadaj rok výroby vozidla: "))
            cena = int(input("Zadaj cenu predaja vozidla v eurách: "))

            auto = Auto(znacka, model, rok, cena)
            auta.append(auto)
            print("\nAuto bolo úspešne pridáne do zoznamu aút na predaj.")   # po vypisani istých špecifikacií nám program zapíše vozidlo do zoznamu a oboznámi nás, následne program nás vráti na menu

        elif vyber == "2":
            if not auta:
                print("\nV zozname nie je žiadne vozidlo.") # pokial v zozname neexistuje žiadne vozidlo, ktoré je zapisané na predaj tak program vypíše, že žiadne auto nie je v zozname a vráti naspäť na menu
            else:
                print("\nZoznam vozidiel: ") # ak sme do zoznamu pridali vozidlo, tak po zvolení čísla 2 nám vypíše zoznam vozidiel, ktoré sme pridali a vráti nás na menu
                for a in auta:
                    print(a)
                print()  
            while True:
                znova = input("\nChceš sa vrátiť naspäť do menu? ").lower() # po vypisani zoznamu sa program opýta či chceme isť naspat do menu, ak ano vrati nas do menu, ak napisene nie skonci interakciu
                if znova == "ano":
                    break
                else: 
                    znova == "nie"
                    return
                  
        elif vyber == "3": 
            print("\nPrajem pekný den.") # po zvolení čísla 3 skončí operácia s menu a program Vám zaželá pekný deň
            break

        else:
            print("\nNeplatná operácia.") # po zvolení iného čísla ako máme v ponuke, program vypíše neplatnu operáciu a vratí naspäť na menu.

if __name__ == "__main__":            
    main()