import requests
import json

page_Scrape_FEARGOD_Hoodie = requests.get('https://ac.cnstrc.com/search/fear%20god?c=ciojs-client-2.35.2&key=key_XT7bjdbvjgECO5d8&i=7111badd-e446-4163-9f53-cd74c5609a72&s=1&page=1&num_results_per_page=24&sort_by=relevance&sort_order=descending&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&variations_map=%7B%22group_by%22%3A%5B%7B%22name%22%3A%22product_condition%22%2C%22field%22%3A%22data.product_condition%22%7D%2C%7B%22name%22%3A%22box_condition%22%2C%22field%22%3A%22data.box_condition%22%7D%5D%2C%22values%22%3A%7B%22min_regional_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_lowest_price_cents_3%22%7D%2C%22min_regional_instant_ship_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_instant_ship_lowest_price_cents_3%22%7D%7D%2C%22dtype%22%3A%22object%22%7D&qs=%7B%22features%22%3A%7B%22display_variations%22%3Atrue%7D%2C%22feature_variants%22%3A%7B%22display_variations%22%3A%22matched%22%7D%7D&_dt=1720482760967')
FEARGOD_Hoodie_output = json.loads(page_Scrape_FEARGOD_Hoodie.text)
FEARGOD_Hoodie = FEARGOD_Hoodie_output['response']['results'][0]['value']
FEARGOD_Hoodie_price = 50

def data_Mens_Hoodies():
    data_Mens_Hoodies = [
        {'name': FEARGOD_Hoodie, 'brand': 'Fear God', 'category': 'Hoodies','gender': 'Male', 'price': FEARGOD_Hoodie_price, 'Website': "https://www.goat.com/apparel/fear-of-god-essentials-pullover-hoodie-stretch-limo-192su224410f"}
    # This is where we can add more hoodies for future endevours
    ]
    return data_Mens_Hoodies