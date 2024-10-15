import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        columns = ['image_url', 'product_name', 'unit', 'quantity', 'price', 'mrp', 'unavailable_quantity', 'url', 'discount']
        df = pd.DataFrame(self.data, columns=columns)
        df_unique = df.drop_duplicates()
        df_filtered = df_unique[df_unique['discount'] >= 50]
        df_sorted = df_filtered.sort_values(by='discount', ascending=False)
        return df_sorted

    def save_to_excel(self, df, filename="product_data_disc_above_50.xlsx"):
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")

    def format_product_message(self, row):
        message = (
            f"Price Drop Alert!!!\n"
            f"Product : {row['product_name']}\n"
            f"Discount : {row['discount']}%\n"
            f"Current Price : ₹{row['price']}\n"
            f"MRP : ₹{row['mrp']}\n"
            f"Quantity : {row['quantity']}\n"
            f"Units : {row['unit']}\n"
            f"Image URL : {row['image_url']}\n"
            f"URL : {row['url']}\n"
            "Platform : BlinkIt"
        )
        return message
