from requests import *
import Pokemon

rep = get("https://pokeapi.co/api/v2/pokemon")
print(rep.status_code)
rep = rep.json()
print(rep)







while 1 == 1:
    print("Enter command:")
    command = input()
    if command == 'exit':
        break
    elif command == 'add':
        new_name = input("Enter name:\n")
        req = get("https://pokeapi.co/api/v2/pokemon/" + new_name)
        pokemon = req.json()
        new_pokemon = Pokemon(pokemon)
        print(pokemon)