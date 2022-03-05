import requests
from tokens import lolKey
import json


def lol(champ):
    try:
        url = f"https://league-of-legends-stats.p.rapidapi.com/champions/{champ}/stats"
        headers = {
            'x-rapidapi-host': "league-of-legends-stats.p.rapidapi.com",
            'x-rapidapi-key': lolKey
        }
        responses = requests.request("GET", url, headers=headers)
        response = json.loads(responses.text)
        important = {"Name": response['name'],
                     "HP": response['hp'],
                     "HP gain per level": response['hp_gain_per_lvl'],
                     "HP regen": response['hp_regen'],
                     "mana": response['mana'],
                     "mana gain per level": response['mana_gain_per_lvl'],
                     "Mana regen": response['mana_regen'],
                     "Attack damage": response['attack_damage'],
                     "Attack speed": response['attack_speed'],
                     "Armor": response['armor'],
                     "Magic resist": response['magic_resist'],
                     "Movement speed": response['movement_speed'],
                     "Range": response['range'],
                     "Ability Power": response['ability_power'],
                     "Ability Haste": response['ability_haste'],
                     "Critical": response['crit']}
        return important
    except:
        return "Invalid champion name"
