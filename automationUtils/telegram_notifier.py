import asyncio
import telegram
import time

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.bot = telegram.Bot(token=token)
        self.chat_id = chat_id

    async def send_telegram_alert(self, message):
        await self.bot.send_message(chat_id=self.chat_id, text=message)

    def send_alert_sync(self, message):
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send_telegram_alert(message))
        time.sleep(3)
