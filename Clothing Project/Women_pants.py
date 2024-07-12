import requests
import json

page_Scrape_OFFwhite_Pants_womens = requests.get('https://ac.cnstrc.com/search/pants?c=ciojs-client-2.35.2&key=key_XT7bjdbvjgECO5d8&i=7111badd-e446-4163-9f53-cd74c5609a72&s=1&page=1&num_results_per_page=24&filters%5Bgender%5D=women&sort_by=relevance&sort_order=descending&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&variations_map=%7B%22group_by%22%3A%5B%7B%22name%22%3A%22product_condition%22%2C%22field%22%3A%22data.product_condition%22%7D%2C%7B%22name%22%3A%22box_condition%22%2C%22field%22%3A%22data.box_condition%22%7D%5D%2C%22values%22%3A%7B%22min_regional_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_lowest_price_cents_3%22%7D%2C%22min_regional_instant_ship_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_instant_ship_lowest_price_cents_3%22%7D%7D%2C%22dtype%22%3A%22object%22%7D&qs=%7B%22features%22%3A%7B%22display_variations%22%3Atrue%7D%2C%22feature_variants%22%3A%7B%22display_variations%22%3A%22matched%22%7D%7D&_dt=1720483991100')
OFFwhite_Pants_output_womens = json.loads(page_Scrape_OFFwhite_Pants_womens.text)
OFFwhite_Pants_women = OFFwhite_Pants_output_womens['response']['results'][2]['value']
OFFwhite_Pants_price = 200

def data_Women_Pants():
    data_Women_Pants = [
        {'name': OFFwhite_Pants_women, 'brand': 'OFF-White', 'category': 'Pants','gender': 'Female', 'price': OFFwhite_Pants_price, 'Website': "https://www.goat.com/apparel/off-white-formal-straight-leg-pants-black-owca129s21fab0011000"}
    # This is where we can add more pants for future endevours
    ]
    return data_Women_Pants