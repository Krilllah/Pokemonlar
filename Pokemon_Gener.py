from requests import *
from Pokemon import *

rep = get("https://pokeapi.co/api/v2/pokemon")
print(rep.status_code)
rep = rep.json()
print(rep)
d = {}






while 1 == 1:
    print("Enter command:")
    command = input()
    if command == 'exit':
        break
    elif command == 'add':
        new_name = input("Enter name:\n")
        req = get("https://pokeapi.co/api/v2/pokemon/" + new_name)
        if req.status_code == 404 or new_name == '':
            print('No info bout dis.')
        else:
            if new_name not in d:
                pokemon = req.json()
                new_pokemon = Pokemon(pokemon, new_name)
                d[new_name] = new_pokemon
            d[new_name].print()
