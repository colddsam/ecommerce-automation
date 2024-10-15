import requests
import json

class ProductScraper:
    def __init__(self, location="Kolkata", size="1000"):
        self.queries = ["toy"]
        self.size = size
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7",
            "content-type": "application/json",
            "lat": "22.5726",  # Kolkata Latitude
            "lon": "88.3639"   # Kolkata Longitude
        }

    def scrape_products(self):
        saveData = []
        for query in self.queries:
            url = f"https://blinkit.com/v6/search/products?q={query}&size={self.size}&start=0&search_type=7&collection_name=deal&sort=discount_desc"
            response = requests.get(url, headers=self.headers)

            # Check if the response was successful
            if response.status_code == 200:
                try:
                    data = response.json()
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON response for query: {query}")
                    print(f"Response content: {response.content}")  # Log response for debugging
                    continue

                for objects in data.get('products', []):
                    temp = {}
                    for atc in objects.get('atc_actions_v2', {}).get('default', []):
                        cart_item = atc.get('add_to_cart', {}).get('cart_item', {})
                        temp['image_url'] = cart_item.get('image_url')
                        temp['product_name'] = cart_item.get('product_name')
                        temp['unit'] = cart_item.get('unit')
                        temp['quantity'] = cart_item.get('quantity')
                        temp['price'] = cart_item.get('price')
                        temp['mrp'] = cart_item.get('mrp')
                        temp['unavailable_quantity'] = cart_item.get('unavailable_quantity')
                        prid = cart_item.get('product_id')
                        name = cart_item.get('product_name', '').lower().replace(" ", "-")
                        temp['url'] = f"https://blinkit.com/prn/{name}/prid/{prid}"
                    temp['discount'] = objects.get('discount')
                    saveData.append(temp)
            else:
                # Log any errors
                print(f"Error fetching data for query: {query}")
                print(f"HTTP Status: {response.status_code}")
                print(f"Response content: {response.content}")  # Log response content for debugging

        return saveData
