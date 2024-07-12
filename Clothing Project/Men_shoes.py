import requests
import json

page_Scrape_Nike_Airforces = requests.get('https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=3D359474F39B81EF9684CDA444F5A193&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C8529ff38-7de8-4f69-973c-9fdbfb102ed2)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D')
Nike_AirForces_output = json.loads(page_Scrape_Nike_Airforces.text)
Air_Force_1 = Nike_AirForces_output['data']['products']['products'][1]['title']
Air_Force_1_Price = 115

def data_Mens_Shoes():
    data_Mens_Shoes = [
        {'name': Air_Force_1, 'brand': 'Nike', 'category': 'Shoes','gender': 'Male', 'price': Air_Force_1_Price, 'Website': "https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111"}
    # This is where we can add more shoes for future endevours
    ]
    return data_Mens_Shoes