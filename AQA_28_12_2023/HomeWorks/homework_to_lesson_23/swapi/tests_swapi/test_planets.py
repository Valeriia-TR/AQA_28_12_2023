import json
import pytest
import os


def test_get_planets_without_parameters(planets):
    planets = planets.get_all_planets()
    assert planets.json()["next"] == "https://swapi.dev/api/planets/?page=2"


ddt = {
    'argnames': 'current,previous,next',
    'argvalues': [(1,None,"https://swapi.dev/api/planets/?page=2"),
                  (2,'https://swapi.dev/api/planets/?page=1',"https://swapi.dev/api/planets/?page=3"),
                  (3,'https://swapi.dev/api/planets/?page=2',"https://swapi.dev/api/planets/?page=4"),
                  (4,'https://swapi.dev/api/planets/?page=3',"https://swapi.dev/api/planets/?page=5"),
                  (5,'https://swapi.dev/api/planets/?page=4','https://swapi.dev/api/planets/?page=6'),
                  (6,'https://swapi.dev/api/planets/?page=5',None)]
}


@pytest.mark.parametrize(**ddt)
def test_get_planets_with_parameters(planets,current,previous,next):
    planets = planets.get_all_planets(current)
    assert planets.json()["previous"] == previous
    assert planets.json()["next"] == next


def test_get_single_planet(planets):
    single_planet = planets.get_single_planet()
    assert single_planet.status_code == 200
    assert single_planet.json()["name"] == "Naboo"


def test_save_single_planet(planets):
    planet_id = 10
    planets.save_single_planet(planet_id)
    expected_file_name = 'Kamino_planet.json'
    assert os.path.isfile(expected_file_name), f"File {expected_file_name} was not created."
    if os.path.isfile(expected_file_name):
        with open(expected_file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            assert data['name'] == 'Kamino', "The planet's name in the file is not 'Kamino'."
    os.remove(expected_file_name)


def test_get_single_planet_validate_data_consistency(planets):
    single_planet_response = planets.get_single_planet(8)
    assert single_planet_response.status_code == 200
    single_planet_data = single_planet_response.json()
    with open('Naboo_planet.json', 'r') as file:
        file_data = json.load(file)
    assert file_data == single_planet_data, "Data mismatch between API and local file"


def test_planets_on_5_page(planets):
    page_5 = planets.get_all_planets(5)
    assert page_5.json()["previous"] == "https://swapi.dev/api/planets/?page=4"


def test_save_all_planets(planets):
    planets.save_all_planets()
    with open('All_Planets.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert isinstance(data, list)
        assert len(data) > 0