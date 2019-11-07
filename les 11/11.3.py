import json
JSON = []
while True:
    naam = input("Wat is je achternaam? ")
    if naam == "einde":
        dic_json = json.dumps(JSON, indent=4)

        with open('inloggers.json', 'a') as json_file:
            json_file.writelines(dic_json)
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    dic = {
        "name": naam,
        "voorl": voorl,
        "gbdatum": gbdatum,
        "email": email
        }

    JSON.append(dic)


