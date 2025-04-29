import requests
import random

def get_random_first_gen_pokemon():
    pokemon_id = random.randint(1, 151) #primera generacion
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'name': pokemon_data['name'].capitalize(),
            'id': pokemon_data['id'],
            'height': pokemon_data['height'] / 10,
            'weight': pokemon_data['weight'] / 10,
            'types': [t['type']['name'].capitalize() for t in pokemon_data['types']],
            'abilities': [a['ability']['name'].capitalize() for a in pokemon_data['abilities'] if not a['is_hidden']],
            'hidden_ability': next((a['ability']['name'].capitalize() for a in pokemon_data['abilities'] if a['is_hidden']), None),
            'stats': {s['stat']['name'].capitalize(): s['base_stat'] for s in pokemon_data['stats']}
        }
    else:
        return None

def display_pokemon_info(trainer_name, pokemon):
    print(f"\n¡{trainer_name} ha recibido a {pokemon['name']}!")
    print(f"Pokédex N°: {pokemon['id']}")
    print(f"Tipo(s): {', '.join(pokemon['types'])}")
    print(f"Altura: {pokemon['height']} m")
    print(f"Peso: {pokemon['weight']} kg")
    print(f"Habilidades: {', '.join(pokemon['abilities'])}")
    if pokemon['hidden_ability']:
        print(f"Habilidad Oculta: {pokemon['hidden_ability']}")
    
    print("\nEstadísticas base:")
    for stat, value in pokemon['stats'].items():
        print(f"{stat}: {value}")

def main():
    print("¡Bienvenido al Simulador de Batalla Pokémon!")
    print("(Solo primera generación - Pokémon Rojo/Azul/Amarillo)")
    print("------------------------------------------\n")
    
    # Obtener nombres de los entrenadores
    player_name = input("Ingresa tu nombre: ").strip()
    rival_name = input("Ingresa el nombre de tu rival: ").strip()
    
    print("\n¡Generando Pokémon aleatorios de la primera generación...!")
    
    # Obtener Pokémon para cada jugador
    player_pokemon = get_random_first_gen_pokemon()
    rival_pokemon = get_random_first_gen_pokemon()
    
    # Mostrar información
    if player_pokemon and rival_pokemon:
        display_pokemon_info(player_name, player_pokemon)
        display_pokemon_info(rival_name, rival_pokemon)
        
        print("\n¡Preparados para la batalla!")
        print(f"{player_name} con {player_pokemon['name']} vs {rival_name} con {rival_pokemon['name']}!")
    else:
        print("Hubo un error al obtener los datos de los Pokémon. Intenta nuevamente.")

if __name__ == "__main__":
    main()