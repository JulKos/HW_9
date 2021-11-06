import requests
from pprint import pprint


class Heroes:

    def __init__(self):
        self.heroes_name = {'Hulk', 'Captain America', 'Thanos'}
        self.heroes = {}
        self.max_iq = 0
        self.smartest_hero = 'none'

    def search_hero_name(self):

        for hero in self.heroes_name:
            r = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
            id = r.json()["results"][0]["id"]
            self.heroes[str(id)] = {'name': hero, "iq": 0}
        return self.heroes

    def search_hero_id(self):

        for id in self.heroes:
            r = requests.get(f"https://superheroapi.com/api/2619421814940190/{id}/powerstats")
            intel = r.json()["intelligence"]
            self.heroes[id]['iq'] = intel
        return intel

    def search_smartest_hero(self):

        for id in self.heroes:
            if int(self.heroes[id]['iq']) > self.max_iq:
                self.max_iq = int(self.heroes[id]['iq'])
                self.smartest_hero = self.heroes[id]['name']
        return self.smartest_hero




result = Heroes()
result.search_hero_name()
result.search_hero_id()
print(result.search_smartest_hero())