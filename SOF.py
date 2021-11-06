import requests

from pprint import pprint


class Stackoverflow:

    def get_all_requests(self):
        url = "https://api.stackexchange.com/2.3/questions?fromdate=1635984000&todate=1636156800&order=desc&sort=creation&tagged=python&site=stackoverflow"
        response = requests.get(url, timeout=5)
        return response.json()