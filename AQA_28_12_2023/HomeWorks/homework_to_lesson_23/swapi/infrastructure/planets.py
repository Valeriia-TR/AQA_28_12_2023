from requests import get
from AQA_28_12_2023.HomeWorks.homework_to_lesson_23.swapi.conf import config
import json


class Planets:
    def __init__(self):
        self.__planets_url = f"{config['host1']}planets/"

    def get_all_planets(self, page):
        return get(f'{self.__planets_url}?page={page}')

    def get_single_planet(self, id=8):
        return get(f'{self.__planets_url}{id}/')

    def save_single_planet(self, id):
        response = self.get_single_planet(id)
        if response.status_code == 200:
            planet_data = response.json()
            planet_name = planet_data.get("name", "Unknown")
            filename = f'{planet_name}_planet.json'

            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(planet_data, file, ensure_ascii=False, indent=4)
        else:
            print(f"Failed to retrieve planet with ID {id}. Status Code: {response.status_code}")

    def save_all_planets(self):
        all_planets = []
        page = 1
        while True:
            response = self.get_all_planets(page).json()
            all_planets.extend(response['results'])
            if not response['next']:
                break
            page += 1

        with open('All_Planets.json', 'w', encoding='utf-8') as f:
            json.dump(all_planets, f, ensure_ascii=False, indent=4)