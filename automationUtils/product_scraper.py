import requests
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv

load_dotenv()

endpoint=os.getenv('ENDPOINT')

class ProductScraper:
    def __init__(self, location="Kolkata", size="1000"):
        self.queries = ["toy"]
        self.size = size
        self.geolocator = Nominatim(user_agent="MyApp")
        self.location = self.geolocator.geocode(location)
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7",
            "content-type": "application/json",
            "lat": f"{self.location.latitude}",
            "lon": f"{self.location.longitude}"
        }

    def scrape_products(self):
        save_data = []
        for query in self.queries:
            url = f"{endpoint}?q={query}&size={self.size}&start=0&search_type=7&collection_name=deal&sort=discount_desc"
            response = requests.get(url, headers=self.headers)
            data = response.json()
            for objects in data.get('products', []):
                temp = {}
                for atc in objects.get('atc_actions_v2', {}).get('default', []):
                    temp['image_url'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('image_url')
                    temp['product_name'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('product_name')
                    temp['unit'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('unit')
                    temp['quantity'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('quantity')
                    temp['price'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('price')
                    temp['mrp'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('mrp')
                    temp['unavailable_quantity'] = atc.get('add_to_cart', {}).get('cart_item', {}).get('unavailable_quantity')
                    prid = atc.get('add_to_cart', {}).get('cart_item', {}).get('product_id')
                    name = atc.get('add_to_cart', {}).get('cart_item', {}).get('product_name').lower().replace(" ", "-")
                    temp['url'] = f"https://blinkit.com/prn/{name}/prid/{prid}"
                temp['discount'] = objects.get('discount')
                save_data.append(temp)
        return save_data
