from Pojistenec import Pojistenec


seznam_pojistencu = []
pokracovat = True


while pokracovat == True:

        print("--------------------")
        print("Evidence pojištěných")
        print("--------------------")

        print ("Vyberte si akci")
        print ("1 - Přidat nového pojištěného")
        print ("2 - Vypsat všechny pojištěné")
        print ("3 - Vyhledat pojištěného")
        print ("4 - Konec")

        volba=int(input("Vyberte číslo akce: "))

        if volba == 1:
                jmeno = input("Zadejte jméno pojištěného:\n ").capitalize()
                prijmeni = input("Zadejte přijmení pojištěného:\n  ").capitalize()

                while True:  #ošetření zadání věku jako čísla
                        try:
                                vek = int(input("Zadejte věk pojištěného:\n "))
                                break
                        except ValueError:
                                print("Nesprávný vstup, zadejte platné číslo")

                telefon = input("Zadejte telefon pojištěného:\n  ")
                email = input("Zadejte e-mail:\n  ")
                ulice = input("Zadejte ulici a číslo popisné:\n  ")
                mesto = input("Zadejte město:\n  ")
                psc = input("Zadejte PSČ:\n  ")

                #vytvoření nové instance
                novy_pojistenec=Pojistenec(jmeno,prijmeni,vek,telefon,email,ulice,mesto,psc)
                print (f"Zadali jste pojištěnce:\n {jmeno}\t {prijmeni}")

                # přidání do seznamu pojištěnců
                seznam_pojistencu.append(novy_pojistenec)
                input("\nData byla uložena. Pokračujte libovolnou klávesou...")

        elif volba == 2:  #Výpis pojištěnců

                for pojistenec in seznam_pojistencu:

                    print(pojistenec)


        elif volba == 3: #Vyhledání pojištěnců

                hledane_jmeno = input("Zadejte jméno:\n ").capitalize()
                hledane_prijmeni = input("Zadejte příjmení:\n ").capitalize()

                for pojistenec in seznam_pojistencu:

                        if pojistenec.jmeno == hledane_jmeno and pojistenec.prijmeni == hledane_prijmeni:
                                print(f"Jméno:{pojistenec.jmeno}\t Příjmení: {pojistenec.prijmeni}\t Věk:{pojistenec.vek}")


        else:   #Konec
                print("Děkujeme za použití")
                break