import requests
from time import sleep

class ScryfallCardQuery_v2:
    def __init__(self, query_string):
        self.response = requests.get('https://api.scryfall.com/cards/search?q=' + query_string).json()
        self.data = self.response['data']
        sleep(0.1)
        if self.response['has_more']:
            self.data += self.get_next_pages(self.response['next_page']) 
    
    def get_next_pages(self, next_page):
        next_data = requests.get(next_page).json()

        if next_data['has_more']:
            sleep(0.1)
            return next_data['data'] + self.get_next_pages(next_data['next_page'])
        else:
            return next_data['data']