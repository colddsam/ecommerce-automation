import os
from dotenv import load_dotenv
from automationUtils.product_scraper import ProductScraper
from automationUtils.telegram_notifier import TelegramNotifier
from automationUtils.data_processor import DataProcessor

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

def main():
    
    scraper = ProductScraper()
    product_data = scraper.scrape_products()

    processor = DataProcessor(product_data)
    df_sorted = processor.process_data()

    processor.save_to_excel(df_sorted)

    notifier = TelegramNotifier(TELEGRAM_TOKEN, CHAT_ID)

    for _, row in df_sorted.iterrows():
        message = processor.format_product_message(row)
        notifier.send_alert_sync(message)

    print("Products with >50% discount sent to Telegram successfully.")

if __name__ == "__main__":
    main()