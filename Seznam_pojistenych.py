Seznam_pojistenych = [{
        "Jméno": "Petr",
        "Příjmeni": "Novák",
        "Věk": "",
        "Telefon":"602209566",
    }
]

def add_pojisteny(jmeno, prijmeni, vek, telefon):
    new_dictionary = {}
    new_dictionary["Jméno"] = jmeno
    new_dictionary["Příjmeni"] = prijmeni
    new_dictionary["Věk"] = vek
    new_dictionary["Telefon"] = telefon
    Seznam_pojistenych.append(new_dictionary)


add_pojisteny("Marcel", "Matějka", "50", "602 209 566")
print(Seznam_pojistenych)

