import requests
import json

page_Scrape_Nike_AirMax = requests.get('https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=3D359474F39B81EF9684CDA444F5A193&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2Ce9266a2a-2ed2-4e6b-a602-5a3bae7475bb)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D')
Nike_AirMax_output = json.loads(page_Scrape_Nike_AirMax.text)
Air_Max_90_Futura_Women = Nike_AirMax_output['data']['products']['products'][1]['title']
Air_Max_90_Futura_Women_Price = 150

def data_Womens_Shoes():
    data_Womens_Shoes = [
        {'name': Air_Max_90_Futura_Women, 'brand': 'Nike', 'category': 'Shoes','gender': 'Female', 'price': Air_Max_90_Futura_Women_Price, 'Website': "https://www.nike.com/t/air-max-90-futura-womens-shoes-kvRZ4h/HF5052-100"}
    # This is where we can add more shoes for future endevours
    ]
    return data_Womens_Shoes