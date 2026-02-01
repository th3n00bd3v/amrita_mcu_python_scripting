"""
Using the PokéAPI https://pokeapi.co/docs/v2#pokemon-section
fetch the name and height of all 151 Pokémon of the main series.
Create a text document that describes each Pokémon using the information
available in the JSON response.
NOTE: only using 'height' is enough, but if you want more, go crazy.
BONUS: Using your script, create a folder and download the main 'front_default'
       sprites for each Pokémon using requests into that folder.
       Name the files appropriately using the name data from your response.
"""


from pprint import pprint
import requests
import os

def fetch_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url).json()
    return {
        "name": response["name"],
        "height": response["height"],
        "sprite_url": response["sprites"]["front_default"]
    }

def save_pokemon_info(pokemon_data, filename="pokemon_info.txt"):
    with open(filename, "a") as file:
        file.write(f"Name: {pokemon_data['name'].title()}\n")
        file.write(f"Height: {pokemon_data['height']}\n")
        file.write("\n")
        
def download_sprite(pokemon_data, folder="pokemon_sprites"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    sprite_url = pokemon_data["sprite_url"]
    if sprite_url:
        response = requests.get(sprite_url)
        with open(os.path.join(folder, f"{pokemon_data['name']}.png"), "wb") as file:
            file.write(response.content)
            
for pokemon_id in range(1, 152):
    pokemon_data = fetch_pokemon_data(pokemon_id)
    save_pokemon_info(pokemon_data)
    download_sprite(pokemon_data)
    
print(f"Pokémon information and sprites have been saved.Check the folder {pokemon_sprites} for images.")