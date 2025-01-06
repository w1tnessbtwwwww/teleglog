import datetime
from typing import Optional
import telebot

class TelegLog:
    def __init__(self, token: str, chat_id: str):
        self._bot = telebot.TeleBot(token)
        self._chat_id = chat_id

    def send_log(self, template: str):
        self._bot.send_message(self._chat_id, template, parse_mode="Markdown")

    def info(self, message: str):
        template = f"❗**INFO**❗\n{message}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        
        sending = self.send_log(template)
        

    def error(self, message: str, traceback: Optional[str] = None) -> str:

        if traceback:
            template = f"🚨 **ERROR** 🚨\n{message}\n```python\n{traceback}```\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        else:
            template = f"🚨 **ERROR** 🚨\n{message}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        
        sending = self.send_log(template)
        
    def warning(self, message: str) -> str:
        template = f"⚠️ **WARNING** ⚠️\n{message}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        
        sending = self.send_log(template)
        
    def fatal(self, message: str) -> str:
        template = f"🆘 **FATAL** 🆘\n{message}\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        
        sending = self.send_log(template)
