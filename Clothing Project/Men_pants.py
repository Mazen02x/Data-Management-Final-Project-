import requests
import json

page_Scrape_Adidas_Pants = requests.get('https://ac.cnstrc.com/search/pants?c=ciojs-client-2.35.2&key=key_XT7bjdbvjgECO5d8&i=7111badd-e446-4163-9f53-cd74c5609a72&s=1&page=1&num_results_per_page=24&filters%5Bgender%5D=men&filters%5Bbrand%5D=adidas&sort_by=relevance&sort_order=descending&fmt_options%5Bhidden_fields%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_fields%5D=gp_instant_ship_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_lowest_price_cents_3&fmt_options%5Bhidden_facets%5D=gp_instant_ship_lowest_price_cents_3&variations_map=%7B%22group_by%22%3A%5B%7B%22name%22%3A%22product_condition%22%2C%22field%22%3A%22data.product_condition%22%7D%2C%7B%22name%22%3A%22box_condition%22%2C%22field%22%3A%22data.box_condition%22%7D%5D%2C%22values%22%3A%7B%22min_regional_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_lowest_price_cents_3%22%7D%2C%22min_regional_instant_ship_price%22%3A%7B%22aggregation%22%3A%22min%22%2C%22field%22%3A%22data.gp_instant_ship_lowest_price_cents_3%22%7D%7D%2C%22dtype%22%3A%22object%22%7D&qs=%7B%22features%22%3A%7B%22display_variations%22%3Atrue%7D%2C%22feature_variants%22%3A%7B%22display_variations%22%3A%22matched%22%7D%7D&_dt=1720483687542')
Adidas_Pants_output = json.loads(page_Scrape_Adidas_Pants.text)
Adidas_Pants = Adidas_Pants_output['response']['results'][0]['value']
Adidas_Pants_price = 130

def data_Mens_Pants():
    data_Mens_Pants = [
        {'name': Adidas_Pants, 'brand': 'Adidas', 'category': 'Pants','gender': 'Male', 'price': Adidas_Pants_price, 'Website': "https://www.goat.com/apparel/adidas-x-white-statement-track-suit-pants-chalk-white-im8395"}
    # This is where we can add more pants for future endevours
    ]
    return data_Mens_Pants

